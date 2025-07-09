from faker import Faker
import pandas as pd
import random
from datetime import datetime

n = 1000 # jumlah data

faker = Faker('id_ID') # ini agar nanti generate nama orang-orang indonesia bukan orang luar negeri




gaya_belajar = ['Visual', 'Auditori', 'Kinestetik']
metode_belajar = ['Offline', 'Online']
topik = [
    'Kalkulus 2', 'Matematika 2', 'Dasar Pemrograman', 'Struktur Data',
    'Fisika Listrik', 'Kimia Murni', 'Fisika Magnet', 'Probabilitas & Statistika',
    'Aljabar Linier', 'Fisika Dasar', 'Logika Matematika', 'Pengantar AI',
    'Basis Data', 'Analisis Numerik', 'Metode Statistik'
]





''' 
Okee jika ingin waktu dalam format tanggal dan jam, jadi gw harus bisa generate data random untuk date dan waktunya

1. Kalau pakai datetime apakah bisa ya?, ternyata bisa pakai faker

'''
# Buat objek datetime untuk rentang
start = datetime(2025, 7, 1, 0, 0, 0)
end   = datetime(2025, 12, 31, 23, 59, 59)

# Generate satu datetime acak di antara keduanya
waktu = faker.date_time_between(start_date=start, end_date=end)

