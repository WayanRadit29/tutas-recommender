from faker import Faker
from datetime import timedelta
import random

def get_faker(LOCALE: str) -> Faker:
    ''' Mengembalikan faker '''
    return Faker(LOCALE)

def random_window(faker, start, end, max_span_hours= 3):
    ''' Ini akan mengembalikan nilai tanggal dan jam awal serta tanggal dan jam selesai belajar '''
    base = faker.date_time_between(start, end)
    span = timedelta(hours=random.randint(1, max_span_hours))
    
    return base, base + span

def random_choice_weighted(options, weights=None):
    return random.choices(options, weights=weights, k=1)[0]