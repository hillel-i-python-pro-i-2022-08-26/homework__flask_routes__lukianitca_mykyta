from faker import Faker


def generate_users(users_number: int = 100):
    fake = Faker()
    return (f"{fake.first_name()} {fake.email()}" for _ in range(users_number))
