import pandas as pd
import random
from config import NUM_DATA, GAYA_BELAJAR, METODE_BELAJAR, TOPIK, LOCALE, START_DT, END_DT, FLEX_RATE
from utils import get_faker, random_window, random_choice_weighted, has_overlap
from datetime import datetime, timedelta

# Initialize Faker with Indonesian locale for generating realistic names & phone numbers
faker = get_faker(LOCALE)


def generate_murid():
    """
    Generate synthetic student ("murid") profiles.

    Each student record includes:
        - Unique ID (e.g., M0001)
        - Name (Indonesian-style, generated with Faker)
        - Learning style preference (Visual, Auditory, Kinesthetic)
        - Learning mode (Offline or Online)
        - Preferred subject/topic (from TOPIK list)
        - Availability window (start and end datetime)
        - Flexibility flag (whether schedule can be adjusted)
        - WhatsApp contact number

    Returns:
        pd.DataFrame: A DataFrame containing NUM_DATA student records.
    """
    rows = []
    for i in range(1, NUM_DATA + 1):

        # Generate a random availability window within the global date range
        start, end = random_window(faker, START_DT, END_DT)

        # Assign schedule flexibility with probability = FLEX_RATE
        is_flexible = random.random() < FLEX_RATE

        # Assign random learning preferences
        gaya = random.choice(GAYA_BELAJAR)           # learning style
        metode = random.choice(METODE_BELAJAR)       # mode of learning
        topik_ = random_choice_weighted(TOPIK)       # preferred subject/topic

        # Build one student record
        rows.append({
            'id_murid':         f'M{i:04d}',  # student ID with zero padding
            'nama':             f"{faker.first_name()} {faker.last_name()}",
            'gaya_belajar':     gaya,
            'metode_belajar':   metode,
            'preferensi_topik': topik_,
            'available_start':  start.strftime('%Y-%m-%d %H:%M'),
            'available_end':    end.strftime('%Y-%m-%d %H:%M'),
            'is_flexible':      is_flexible,
            'whatsapp':         faker.phone_number()
        })

    return pd.DataFrame(rows)




def generate_tutor(df_murid):
    """
    Generate synthetic tutor profiles.

    Rules for availability:
        - 70% of tutors have schedules overlapping with a randomly selected student
          (±3 hours around the student's availability).
        - 30% of tutors are assigned a fully random availability window.

    Each tutor record includes:
        - Unique ID (e.g., T0001)
        - Name (Indonesian-style, generated with Faker)
        - Learning style and teaching mode
        - Subject expertise (selected from TOPIK list)
        - Teaching history (rating, total teaching hours)
        - Availability window (start and end datetime)
        - Flexibility flag (whether schedule can be adjusted)
        - WhatsApp contact number

    Args:
        df_murid (pd.DataFrame): Student dataset, used as reference for assigning overlapping schedules.

    Returns:
        pd.DataFrame: A DataFrame containing NUM_DATA tutor records.
    """
    rows = []
    for i in range(1, NUM_DATA + 1):

        # 1. Select one random student to serve as the reference for availability
        murid = df_murid.sample(1).iloc[0]
        murid_start = datetime.strptime(murid['available_start'], "%Y-%m-%d %H:%M")

        # 2. Decide tutor availability:
        #    - 70% overlap with the student's availability (±3 hours offset)
        #    - 30% assigned a fully random slot
        if random.random() < 0.7:
            offset_hr = random.randint(-3, 3)   # small offset around student’s time
            start = murid_start + timedelta(hours=offset_hr)
        else:
            start, _ = random_window(faker, START_DT, END_DT)

        # 3. Define teaching session duration (1–3 hours)
        span_hr = random.randint(1, 3)
        end = start + timedelta(hours=span_hr)

        # 4. Assign tutor attributes
        is_flexible = random.random() < FLEX_RATE
        gaya        = random.choice(GAYA_BELAJAR)     # teaching style
        metode      = random.choice(METODE_BELAJAR)   # delivery mode
        keahlian    = random_choice_weighted(TOPIK)   # subject expertise
        rating      = round(random.uniform(3.0, 5.0), 2)
        total_jam   = random.randint(10, 400)

        # 5. Build one tutor record
        rows.append({
            'id_tutor':         f'T{i:04d}',
            'nama':             f"{faker.first_name()} {faker.last_name()}",
            'gaya_belajar':     gaya,
            'metode_belajar':   metode,
            'keahlian_topik':   keahlian,
            'rating':           rating,
            'total_jam_ngajar': total_jam,
            'available_start':  start.strftime("%Y-%m-%d %H:%M"),
            'available_end':    end.strftime("%Y-%m-%d %H:%M"),
            'is_flexible':      is_flexible,
            'whatsapp':         faker.phone_number()
        })

    return pd.DataFrame(rows)


def generate_interaksi(df_murid, df_tutor, total_row=2000, pos_ratio=0.7):
    """
    Generate synthetic interaction records between students and tutors.

    Interactions are labeled to simulate training data for a recommendation or
    matching model.

    Labeling rules:
        - Positive (label=1):
            * Topic, learning style, and learning mode all match, AND
            * Either the availability windows overlap OR at least one party is flexible.

        - Negative (label=0): Three types, evenly distributed
            1) All features mismatch (topic, style, mode).
            2) Features match, but no time overlap AND neither student nor tutor is flexible.
            3) Features match, no time overlap, but at least one is flexible.
               (Special case: feedback_score determines label —
                score >= 4 → label=1, otherwise label=0)

    Args:
        df_murid (pd.DataFrame): Student dataset.
        df_tutor (pd.DataFrame): Tutor dataset.
        total_row (int, optional): Total number of interaction records to generate. Default is 2000.
        pos_ratio (float, optional): Proportion of positive samples. Default is 0.7.

    Returns:
        pd.DataFrame: Synthetic dataset of interactions, including match flags,
                      flexibility, feedback score, and label.
    """
    rows = []

    # 1. Calculate how many positive and negative samples are needed
    num_pos = int(total_row * pos_ratio)
    num_neg = total_row - num_pos
    num_neg_all = num_neg // 3             # type 1: all features mismatch
    num_neg_time = num_neg // 3            # type 2: time mismatch, no flexibility
    num_neg_time_but_flex = num_neg // 3   # type 3: time mismatch, but flexible

    # ------------------------------------------------------------------
    # 2. Generate positive interactions
    # ------------------------------------------------------------------
    pos_count = 0
    while pos_count < num_pos:
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        # Check feature match (topic, style, mode)
        match_fitur = (
            murid['preferensi_topik'] == tutor['keahlian_topik'] and
            murid['gaya_belajar']     == tutor['gaya_belajar'] and
            murid['metode_belajar']   == tutor['metode_belajar']
        )
        if not match_fitur:
            continue

        # Parse availability windows into datetime objects
        m_start = datetime.strptime(murid['available_start'], "%Y-%m-%d %H:%M")
        m_end   = datetime.strptime(murid['available_end'],   "%Y-%m-%d %H:%M")
        t_start = datetime.strptime(tutor['available_start'], "%Y-%m-%d %H:%M")
        t_end   = datetime.strptime(tutor['available_end'],   "%Y-%m-%d %H:%M")

        # Check if time overlaps or if at least one party is flexible
        overlap = has_overlap(m_start, m_end, t_start, t_end)
        fleksibel = murid['is_flexible'] or tutor['is_flexible']
        if not (overlap or fleksibel):
            continue

        # Save positive record
        rows.append({
            'id_murid':       murid['id_murid'],
            'id_tutor':       tutor['id_tutor'],
            'topik_match':    True,
            'gaya_match':     True,
            'metode_match':   True,
            'time_overlap':   overlap,
            'murid_flexible': murid['is_flexible'],
            'tutor_flexible': tutor['is_flexible'],
            'feedback_score': random.choices([4, 5], weights=[0.4, 0.6])[0],
            'label':          1
        })
        pos_count += 1

    # ------------------------------------------------------------------
    # 3a. Negative interactions: all features mismatch
    # ------------------------------------------------------------------
    neg_all_count = 0
    while neg_all_count < num_neg_all:
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        if (
            murid['preferensi_topik'] != tutor['keahlian_topik'] and
            murid['gaya_belajar']     != tutor['gaya_belajar'] and
            murid['metode_belajar']   != tutor['metode_belajar']
        ):
            rows.append({
                'id_murid':       murid['id_murid'],
                'id_tutor':       tutor['id_tutor'],
                'topik_match':    False,
                'gaya_match':     False,
                'metode_match':   False,
                'time_overlap':   False,
                'murid_flexible': murid['is_flexible'],
                'tutor_flexible': tutor['is_flexible'],
                'feedback_score': 0,
                'label':          0
            })
            neg_all_count += 1

    # ------------------------------------------------------------------
    # 3b. Negative interactions: features match, time mismatch, no flexibility
    # ------------------------------------------------------------------
    neg_time_count = 0
    while neg_time_count < num_neg_time:
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        # Require feature match
        if not (
            murid['preferensi_topik'] == tutor['keahlian_topik'] and
            murid['gaya_belajar']     == tutor['gaya_belajar'] and
            murid['metode_belajar']   == tutor['metode_belajar']
        ):
            continue

        # Parse availability windows
        m_start = datetime.strptime(murid['available_start'], "%Y-%m-%d %H:%M")
        m_end   = datetime.strptime(murid['available_end'],   "%Y-%m-%d %H:%M")
        t_start = datetime.strptime(tutor['available_start'], "%Y-%m-%d %H:%M")
        t_end   = datetime.strptime(tutor['available_end'],   "%Y-%m-%d %H:%M")

        # Must have no overlap and no flexibility
        if has_overlap(m_start, m_end, t_start, t_end):
            continue
        if murid['is_flexible'] or tutor['is_flexible']:
            continue

        rows.append({
            'id_murid':       murid['id_murid'],
            'id_tutor':       tutor['id_tutor'],
            'topik_match':    True,
            'gaya_match':     True,
            'metode_match':   True,
            'time_overlap':   False,
            'murid_flexible': False,
            'tutor_flexible': False,
            'feedback_score': 0,
            'label':          0
        })
        neg_time_count += 1

    # ------------------------------------------------------------------
    # 3c. Negative interactions: features match, time mismatch, but flexible
    # ------------------------------------------------------------------
    neg_time_but_flex_count = 0
    while neg_time_but_flex_count < num_neg_time_but_flex:
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        # Require feature match
        if not (
            murid['preferensi_topik'] == tutor['keahlian_topik'] and
            murid['gaya_belajar']     == tutor['gaya_belajar'] and
            murid['metode_belajar']   == tutor['metode_belajar']
        ):
            continue

        # Parse availability windows
        m_start = datetime.strptime(murid['available_start'], "%Y-%m-%d %H:%M")
        m_end   = datetime.strptime(murid['available_end'],   "%Y-%m-%d %H:%M")
        t_start = datetime.strptime(tutor['available_start'], "%Y-%m-%d %H:%M")
        t_end   = datetime.strptime(tutor['available_end'],   "%Y-%m-%d %H:%M")

        # Require no overlap but at least one party flexible
        if has_overlap(m_start, m_end, t_start, t_end):
            continue
        if not murid['is_flexible'] and not tutor['is_flexible']:
            continue

        feedback_score = random.randint(1, 5)
        rows.append({
            'id_murid':       murid['id_murid'],
            'id_tutor':       tutor['id_tutor'],
            'topik_match':    True,
            'gaya_match':     True,
            'metode_match':   True,
            'time_overlap':   False,
            'murid_flexible': murid['is_flexible'],
            'tutor_flexible': tutor['is_flexible'],
            'feedback_score': feedback_score,
            # Flexible case: label depends on feedback score
            'label':          1 if feedback_score >= 4 else 0
        })
        neg_time_but_flex_count += 1

    return pd.DataFrame(rows)
