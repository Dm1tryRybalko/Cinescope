import pytest
from constants import BASE_URL

def check_total_difference(dict1, dict2):
    for key in dict1:
        if key in dict2:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                if not check_total_difference(dict1[key], dict2[key]):
                    return False
            elif dict1[key] == dict2[key]:
                return False
    return True


class TestBookingPositive:

    def test_create_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data[
            "totalprice"], "Заданная стоимость не совпадает"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Заданная фамилия не совпадает"
        created_booking = get_booking.json()
        return [booking_id, created_booking]

    def test_delete_booking(self, auth_session, booking_data):
        created_booking_info = self.test_create_booking(auth_session, booking_data)
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{created_booking_info[0]}")
        assert deleted_booking.status_code == 201, "Бронь не удалилась"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{created_booking_info[0]}")
        assert get_booking.status_code == 404, "Бронь не удалилась"

    def test_update_booking(self, auth_session, booking_data, booking_data_changed):
        created_booking_info = self.test_create_booking(auth_session, booking_data)
        put_booking = auth_session.put(f"{BASE_URL}/booking/{created_booking_info[0]}", json=booking_data_changed)
        assert put_booking.status_code == 200, "Ошибка при обновлении брони"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{created_booking_info[0]}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert check_total_difference(created_booking_info[1], get_booking.json()), "Есть одинаковые данные"

    def test_partial_update(self, auth_session, booking_data, booking_data_partial):
        created_booking_info = self.test_create_booking(auth_session, booking_data)
        patch_booking = auth_session.patch(f"{BASE_URL}/booking/{created_booking_info[0]}", json=booking_data_partial)
        assert patch_booking.status_code == 200, "Ошибка при обновлении брони"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{created_booking_info[0]}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json().get('firstname') != created_booking_info[1].get("firstname"), "Одинаковые firstnames"
        assert get_booking.json().get('additionalneeds') != created_booking_info[1].get("additionalneeds"), "Одинаковые additionalneeds"


class TestBookingNegative:

    def test_neg_get_bookingids(self, auth_session, booking_data_corrupted):
        get_bookings = auth_session.get(f"{BASE_URL}/booking",
                                        params={"firstname": booking_data_corrupted["firstname"]})
        assert isinstance(get_bookings.json(), list), "Вернулся тип данных отличный от list"
        assert len(get_bookings.json()) == 0, "Были найдены брони с некорректным именем"

    def test_neg_get_booking(self, auth_session):
        get_booking = auth_session.get(f"{BASE_URL}/booking/abc")
        assert get_booking.status_code == 404, "Найдена бронь с неверным id"

    def test_neg_create_booking(self, auth_session, booking_data_corrupted):
        created_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data_corrupted)
        assert created_booking.status_code == 500, "Ожидали ошибку 500"
        self.test_neg_get_bookingids(auth_session, booking_data_corrupted)

    def test_update_booking_neg(self, auth_session, booking_data, booking_data_corrupted):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data_corrupted)
        assert update_booking.status_code == 500, "Ожидалась ошибка 500"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.json() == booking_data, "Оригинальная бронь отличается"

    def test_partial_update_booking_neg(self, auth_session, booking_data, booking_data_corrupted):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        partial_update = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data_corrupted)
        assert partial_update.status_code == 500, "Ожидалась ошибка 500"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.json() == booking_data, "Данные были изменены на невалидные"

    def test_delete_booking_neg(self, auth_session, booking_data, get_random_string):
        # create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        # assert create_booking.status_code == 200, "Ошибка при создании брони"
        # booking_id = create_booking.json().get("bookingid")
        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{get_random_string}")
        assert deleted_booking.status_code == 405, "Ожидали ошибку 405"








