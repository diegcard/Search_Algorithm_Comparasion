import random
from search import constants


def get_random_sorted_list(size, limit=constants.MAX_VALUE):
    """Generates a sorted list of random integers"""
    arr = [random.randint(0, limit) for _ in range(size)]
    return sorted(arr)
