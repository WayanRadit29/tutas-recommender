from datetime import datetime

NUM_DATA = 1000
GAYA_BELAJAR = ['Visual', 'Auditori', 'Kinestetik']
METODE_BELAJAR = ['Offline', 'Online']
TOPIK = [
    'Kalkulus 2', 'Matematika 2', 'Dasar Pemrograman', 'Struktur Data',
    'Fisika Listrik', 'Kimia Murni', 'Fisika Magnet', 'Probabilitas & Statistika',
    'Aljabar Linier', 'Fisika Dasar', 'Logika Matematika', 'Pengantar AI',
    'Basis Data', 'Analisis Numerik', 'Metode Statistik'
]

LOCALE = 'id_ID' # ini untuk kode indonesia di library Faker, jadi nanti akan generate nama orang indonesia
START_DT   = datetime(2025,7,1)
END_DT     = datetime(2025,12,31)
FLEX_RATE  = 0.3