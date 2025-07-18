import pandas as pd
import random
from config import NUM_DATA, GAYA_BELAJAR, METODE_BELAJAR, TOPIK, LOCALE, START_DT, END_DT, FLEX_RATE
from utils import get_faker, random_window, random_choice_weighted, has_overlap
from datetime import datetime, timedelta

faker = get_faker(LOCALE)

'''
Okee jadi disini gw pengen agar waktu tutor overlap dengan murid sebanyak 70 persen, sisanya beda dan bisa fleksibel dan tidak

Jadi yang harus gw lakukan adalah :
1. 
'''
def generate_murid():
    rows = []
    for i in range(1, NUM_DATA + 1):

        # Time Window
        start, end = random_window(faker, START_DT, END_DT)

        # Fleksibilitas
        is_flexible = random.random() < FLEX_RATE

        # Pilihan lain
        gaya = random.choice(GAYA_BELAJAR)
        metode = random.choice(METODE_BELAJAR)
        topik_ = random_choice_weighted(TOPIK)

        # Bangun data satu baris untuk murid
        # 4) Bangun record
        rows.append({
                'id_murid':         f'M{i:04d}',
                'nama':             f"{faker.first_name()}  {faker.last_name()}",
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
    rows = []
    for i in range(1, NUM_DATA+1):
        # 1) Ambil satu murid acak sebagai basis slot
        murid = df_murid.sample(1).iloc[0]
        # parse available_start string jadi datetime
        murid_start = datetime.strptime(murid['available_start'], "%Y-%m-%d %H:%M")
        

        # 2) Tentukan apakah overlap (70%) atau random (30%)
        if random.random() < 0.7:
            # hitung offset jam antara -3..+3
            offset_hr = random.randint(-3, 3)
            start = murid_start + timedelta(hours=offset_hr)
        else:
            # random penuh di rentang global
            start, _ = random_window(faker, START_DT, END_DT)

        # 3) Buat durasi 1–3 jam
        span_hr = random.randint(1, 3)
        end     = start + timedelta(hours=span_hr)

        # 4) Flags & data lain
        is_flexible = random.random() < FLEX_RATE
        whatsapp    = faker.phone_number()
        gaya        = random.choice(GAYA_BELAJAR)
        metode      = random.choice(METODE_BELAJAR)
        keahlian    = random_choice_weighted(TOPIK)
        rating      = round(random.uniform(3.0,5.0),2)
        total_jam   = random.randint(10,400)

        rows.append({
          'id_tutor':        f'T{i:04d}',
          'nama':            f"{faker.first_name()} {faker.last_name()}",
          'gaya_belajar':    gaya,
          'metode_belajar':  metode,
          'keahlian_topik':  keahlian,
          'rating':          rating,
          'total_jam_ngajar':total_jam,
          'available_start': start.strftime("%Y-%m-%d %H:%M"),
          'available_end':   end.strftime("%Y-%m-%d %H:%M"),
          'is_flexible':     is_flexible,
          'whatsapp':        whatsapp
        })
    return pd.DataFrame(rows)


'''
Kita akan membuat data yang variasi dan positif dan negatif agar bisa dipelajari oleh model nantinya
    
Parameter fungsi :
1. ratio positif
2. jumlah data
3. 
'''
def generate_interaksi(df_murid, df_tutor, total_row=2000, pos_ratio=0.7):
    """
    Generate synthetic interaction records for training.
    
    Positive (label=1):  topik, gaya, metode all match AND
                         (time overlap OR either is flexible)
    Negative (label=0):  two types, split evenly among negatives
      1) all features mismatch
      2) topik, gaya, metode match AND time mismatch AND neither flexible
    """
    rows = []
    # 1. hitung jumlah positif & negatif
    num_pos = int(total_row * pos_ratio)
    num_neg = total_row - num_pos
    num_neg_all = num_neg // 2
    num_neg_time = num_neg - num_neg_all

    # 2. buat interaksi positif
    pos_count = 0
    while pos_count < num_pos:
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        # cek match fitur
        match_fitur = (
            murid['preferensi_topik'] == tutor['keahlian_topik'] and
            murid['gaya_belajar']       == tutor['gaya_belajar'] and
            murid['metode_belajar']     == tutor['metode_belajar']
        )
        if not match_fitur:
            continue

        # parse waktu
        m_start = datetime.strptime(murid['available_start'], "%Y-%m-%d %H:%M")
        m_end   = datetime.strptime(murid['available_end'],   "%Y-%m-%d %H:%M")
        t_start = datetime.strptime(tutor['available_start'], "%Y-%m-%d %H:%M")
        t_end   = datetime.strptime(tutor['available_end'],   "%Y-%m-%d %H:%M")

        # cek overlap atau fleksibel
        overlap = has_overlap(m_start, m_end, t_start, t_end)
        fleksibel = murid['is_flexible'] or tutor['is_flexible']
        if not (overlap or fleksibel):
            continue

        # simpan record positif
        rows.append({
            'id_murid':           murid['id_murid'],
            'id_tutor':           tutor['id_tutor'],
            'topik_match':        True,
            'gaya_match':         True,
            'metode_match':       True,
            'time_overlap':       overlap,
            'murid_flexible':     murid['is_flexible'],
            'tutor_flexible':     tutor['is_flexible'],
            'label':              1
        })
        pos_count += 1

    # 3a. buat interaksi negatif: semua fitur mismatch
    neg_all_count = 0
    while neg_all_count < num_neg_all:
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        # pastikan semua fitur mismatch
        if (
            murid['preferensi_topik'] != tutor['keahlian_topik'] and
            murid['gaya_belajar']       != tutor['gaya_belajar'] and
            murid['metode_belajar']     != tutor['metode_belajar']
        ):
            rows.append({
                'id_murid':           murid['id_murid'],
                'id_tutor':           tutor['id_tutor'],
                'topik_match':        False,
                'gaya_match':         False,
                'metode_match':       False,
                'time_overlap':       None,
                'murid_flexible':     murid['is_flexible'],
                'tutor_flexible':     tutor['is_flexible'],
                'label':              0
            })
            neg_all_count += 1

    # 3b. buat interaksi negatif: fitur match tapi waktu mismatch & tidak fleksibel
    neg_time_count = 0
    while neg_time_count < num_neg_time:
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        # fitur harus match
        if not (
            murid['preferensi_topik'] == tutor['keahlian_topik'] and
            murid['gaya_belajar']       == tutor['gaya_belajar'] and
            murid['metode_belajar']     == tutor['metode_belajar']
        ):
            continue

        # parse waktu
        m_start = datetime.strptime(murid['available_start'], "%Y-%m-%d %H:%M")
        m_end   = datetime.strptime(murid['available_end'],   "%Y-%m-%d %H:%M")
        t_start = datetime.strptime(tutor['available_start'], "%Y-%m-%d %H:%M")
        t_end   = datetime.strptime(tutor['available_end'],   "%Y-%m-%d %H:%M")

        # harus mismatch waktu & keduanya tidak fleksibel
        if has_overlap(m_start, m_end, t_start, t_end):
            continue
        if murid['is_flexible'] or tutor['is_flexible']:
            continue

        rows.append({
            'id_murid':           murid['id_murid'],
            'id_tutor':           tutor['id_tutor'],
            'topik_match':        True,
            'gaya_match':         True,
            'metode_match':       True,
            'time_overlap':       False,
            'murid_flexible':     False,
            'tutor_flexible':     False,
            'label':              0
        })
        neg_time_count += 1

    return pd.DataFrame(rows)
