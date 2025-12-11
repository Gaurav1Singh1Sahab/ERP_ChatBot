import random

COUNTRIES = ["USA","India","UK","Germany","Canada","France","Japan"]

def random_author() -> str:
    return f"Author_{random.randint(1000,9999)}"

def random_country() -> str:
    return random.choice(COUNTRIES)
