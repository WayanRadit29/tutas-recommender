import pandas as pd
import random
from config import NUM_DATA, GAYA_BELAJAR, METODE_BELAJAR, TOPIK, LOCALE, START_DT, END_DT, FLEX_RATE
from utils import get_faker, random_window, random_choice_weighted

faker = get_faker(LOCALE)

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
                'nama':             faker.name(),
                'gaya_belajar':     gaya,
                'metode_belajar':   metode,
                'preferensi_topik': topik_,
                'available_start':  start.strftime('%Y-%m-%d %H:%M'),
                'available_end':    end.strftime('%Y-%m-%d %H:%M'),
                'is_flexible':      is_flexible,
                'whatsapp':         faker.phone_number()
            })

    return pd.DataFrame(rows)


def generate_tutor():
    rows = []

    for i in range(1, NUM_DATA + 1):
        start, end = random_window(faker, START_DT, END_DT)
        is_flexible = random.random() < FLEX_RATE
        whatsapp    = faker.phone_number() 
        gaya        = random.choice(GAYA_BELAJAR)
        metode      = random.choice(METODE_BELAJAR)
        keahlian    = random_choice_weighted(TOPIK)
        rating      = round(random.uniform(3.0, 5.0), 2)
        total_jam   = random.randint(10, 400)


        rows.append({
            'id_tutor':         f'T{i:04d}',
            'nama':             faker.name(),
            'gaya_belajar':     gaya,
            'metode_belajar':   metode,
            'keahlian_topik':   keahlian,
            'rating':           rating,
            'total_jam_ngajar': total_jam,
            'available_start':  start.strftime('%Y-%m-%d %H:%M'),
            'available_end':    end.strftime('%Y-%m-%d %H:%M'),
            'is_flexible':      is_flexible,
            'whatsapp':         whatsapp
        })

    return pd.DataFrame(rows)

def generate_interaksi(df_murid, df_tutor):
    rows = []

    '''Untuk kita membuat data interaksi tutor dan murid , berarti kita perlu untuk memakai data dari generate murid dan tutor, '''
    for _ in range(NUM_DATA * 2):
        murid = df_murid.sample(1).iloc[0]
        tutor = df_tutor.sample(1).iloc[0]

        tanggal = faker.date_time_between(start_date=START_DT, end_date=END_DT)
        durasi = random.choice([30, 45, 60, 90, 120, 180])
        feedback = random.randint(1, 5)

        rows.append(
            {

            'id_murid':  murid['id_murid'],
            'id_tutor':  tutor['id_tutor'],
            'tanggal':   tanggal.strftime('%Y-%m-%d %H:%M'),
            'durasi':    durasi,
            'feedback':  feedback


            }
        )
    return pd.DataFrame(rows)

