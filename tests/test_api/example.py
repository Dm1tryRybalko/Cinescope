import requests

# booking_id = 1
# response = requests.get(f'https://restful-booker.herokuapp.com/booking/', params={'firstname': 'Mary'})
#
# data = response.json()
#
# print(f"Тело ответа: {data}")
# print(type(data))


# try:
#     response = requests.get('https://restful-booker.herokuapp.com/booking')
#
#     response.raise_for_status()
#
#     data = response.json()
#     print(f"Получены данные: {data}")
#
# except requests.exceptions.ConnectionError:
#     print("Не удалось подключиться к серверу")
#
# except requests.exceptions.Timeout:
#     print("Сервер не отвечает слишком долго")
#
# except requests.exceptions.HTTPError as http_err:
#     print(f"Произошла HTTP ошибка: {http_err}")
#
# except requests.exceptions.RequestException as e:
#     print(f"Произошла ошибка при выполнении запроса: {e}")


# data = {
#     "firstname": "Jim",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": True,
#     "bookingdates": {
#         "checkin": "2025-01-04",
#         "checkout": "2025-01-15"
#     },
#     "additionalneeds": "Breakfast"
# }
#
# URL = 'https://restful-booker.herokuapp.com/booking'
#
#
# response = requests.post(URL, json=data)
# assert response.status_code == 200, "Ожидали код ответа 200"
#
# bookingId = response.json()['bookingid']
# print(bookingId)
# bookingName = response.json()['booking']['firstname']
# print(bookingName)
#
# response2 = requests.get(f"{URL}/{bookingId}")
# assert response2.status_code == 200, "Ожидали код ответа 200"
# assert bookingName == response2.json()['firstname'], "Ожидали, что имена придут одинаковые"


# url = 'https://restful-booker.herokuapp.com/booking'
# payload = {
#     "firstname": "Jim",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": True,
#     "bookingdates": {
#         "checkin": "2025-01-04",
#         "checkout": "2025-01-15"
#     },
#     "additionalneeds": "Breakfast"
# }
#
#
# response = requests.post(url, data=payload)
# print(response.text)
# print(response.request.body)




# import time
#
# url = "https://httpbin.org/get"
# num_requests = 10
#
# print("Запросы с использованием сессии:")
# start_time = time.time()
#
# session = requests.Session()  # Создаем сессию
# try:
#     for i in range(num_requests):
#         response = session.get(url)
#         response.raise_for_status()
# except Exception as e:
#     print(f"ошибка: {e}")
# finally:
#     session.close()  # закрываем сессию
# end_time = time.time()
# print(f"Время выполнения с сессией: {end_time - start_time:.4f} секунд\n")
#
# # Запросы БЕЗ использования сессии:
# print("Запросы БЕЗ использования сессии:")
# start_time = time.time()
# try:
#     for i in range(num_requests):
#         response = requests.get(url)
#         response.raise_for_status()
# except Exception as e:
#     print(f"Ошибка: {e}")
# end_time = time.time()
# print(f"Время выполнения без сессии: {end_time - start_time:.4f} секунд")

