from faker import Faker
import requests
from typing import Generator


def generate_users(users_number: int) -> Generator:
    fake = Faker("uk_UA")
    return (f"{fake.first_name()} {fake.email()}" for _ in range(users_number))


def get_cosmonauts() -> dict:
    return requests.get("http://api.open-notify.org/astros.json").json()
