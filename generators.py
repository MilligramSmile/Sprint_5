import random
import string


def generate_name():
    return f"user_{random.randint(1000, 9999)}@example.com"


def generate_login():
    return f"user_{random.randint(1000, 9999)}@example.com"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
