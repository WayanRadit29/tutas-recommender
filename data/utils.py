from faker import Faker
from datetime import timedelta
import random


def get_faker(LOCALE: str) -> Faker:
    """
    Initialize and return a Faker instance.

    Args:
        LOCALE (str): Locale string (e.g., 'id_ID' for Indonesian).

    Returns:
        Faker: Configured Faker object for generating synthetic names,
               phone numbers, and datetime values.
    """
    return Faker(LOCALE)


def random_window(faker, start, end, max_span_hours: int = 3):
    """
    Generate a random time window within a given date range.

    Args:
        faker (Faker): Faker instance used to generate a random datetime.
        start (datetime): Earliest possible datetime.
        end (datetime): Latest possible datetime.
        max_span_hours (int, optional): Maximum window size in hours.
                                        Default is 3.

    Returns:
        tuple(datetime, datetime): A (start, end) datetime window.
    """
    base = faker.date_time_between(start, end)                 # random start time
    span = timedelta(hours=random.randint(1, max_span_hours))  # random duration
    return base, base + span


def random_choice_weighted(options, weights=None):
    """
    Select one element from a list with optional weighting.

    Args:
        options (list): List of candidate values.
        weights (list, optional): Weights corresponding to each option.

    Returns:
        Any: One randomly selected element from the list.
    """
    return random.choices(options, weights=weights, k=1)[0]


def has_overlap(m_start, m_end, t_start, t_end):
    """
    Check whether two time intervals overlap.

    Args:
        m_start (datetime): Start of first interval.
        m_end (datetime): End of first interval.
        t_start (datetime): Start of second interval.
        t_end (datetime): End of second interval.

    Returns:
        bool: True if intervals overlap, False otherwise.
    """
    return (m_start < t_end) and (m_end > t_start)
