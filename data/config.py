from datetime import datetime

# Number of synthetic data records to generate
NUM_DATA = 1000  

# Categories of learning styles (student preference)
GAYA_BELAJAR = ['Visual', 'Auditory', 'Kinesthetic']

# Modes of learning delivery
METODE_BELAJAR = ['Offline', 'Online']

# Academic subjects to be included in the dataset
TOPIK = [
    'Calculus II', 'Mathematics II', 'Introduction to Programming', 'Data Structures',
    'Electricity Physics', 'Pure Chemistry', 'Magnetism Physics', 'Probability & Statistics',
    'Linear Algebra', 'General Physics', 'Mathematical Logic', 'Introduction to AI',
    'Databases', 'Numerical Analysis', 'Statistical Methods'
]

# Locale setting for Faker library
# 'id_ID' ensures generated names follow Indonesian naming conventions
LOCALE = 'id_ID'  

# Date range for synthetic events (e.g., study sessions, interactions)
START_DT = datetime(2025, 7, 1)
END_DT   = datetime(2025, 12, 31)

# Flexibility rate (e.g., proportion of records where time or preference is adjusted randomly)
FLEX_RATE = 0.3
