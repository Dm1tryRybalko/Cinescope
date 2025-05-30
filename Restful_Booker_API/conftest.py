import pytest
import requests
from faker import Faker
from constants import HEADERS, BASE_URL

faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)

    response = requests.post(
        f"{BASE_URL}/auth",
        headers=HEADERS,
        json={"username": "admin", "password": "password123"}
    )
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    assert token is not None, "В ответе не оказалось токена"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Cigars"
    }

@pytest.fixture
def booking_data_changed():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": "Vodka"
    }

@pytest.fixture
def booking_data_partial():
    return {
        "firstname": faker.first_name(),
        "additionalneeds": "Coke"
    }

@pytest.fixture
def booking_data_corrupted():
    return {
        "firstname": faker.random_number(),
        "lastname": faker.random_int(min=100, max=100000),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": "Vodka"
    }

@pytest.fixture
def get_random_string():
    random_length = faker.random_int(min=1, max=10)
    random_string = ''.join(faker.random_letters(length=random_length))
    return random_string
