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
def generate_interaksi(df_murid, df_tutor, total_row=2000, pos_ratio = 0.5):
    rows = []
    num_pos = total_row * pos_ratio
    num_neg = total_row - num_pos

    # Sekarang buat untuk data yang positif
    





    