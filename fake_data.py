import allure
import requests
from faker import Faker
from test_urls import TestUrls

fake = Faker('ru_RU')


class FakerMethods:
    @staticmethod
    @allure.title('Создание пользователя')
    def create_user():
        email = fake.free_email()
        password = fake.password()
        payload = {
            'email': email,
            'password': password,
            'name': fake.first_name()
        }
        response = requests.post(TestUrls.USER_REGISTER, data=payload)

        if response.status_code == 200:
            response_body = response.json()
            access_token = response_body.get('accessToken')
            return {
                'email': email,
                'password': password,
                'accessToken': access_token
            }
        else:
            raise Exception(f"Failed to create user: {response.status_code} - {response.text}")

    @staticmethod
    @allure.title('Удаление пользователя')
    def delete_user(access_token):
        requests.delete(TestUrls.USER_DELETE, headers={'Authorization': access_token})

    @staticmethod
    def create_order(order_payload, access_token=None):
        payload = {'ingredients': [order_payload]}
        headers = {}
        if access_token:
            headers = {'Authorization': f'{access_token}'}
        response = requests.post(TestUrls.ORDER_CREATE, data=payload, headers=headers)
        return response

    burger = ['61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa72']
