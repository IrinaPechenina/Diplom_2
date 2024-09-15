import allure
import requests
import data


class TestGetUserOrder:

    @allure.title('Проверка ручки /api/order. '
                  '1.авторизованный пользователь может получить свои заказы'
                  '2.успешный запрос возвращает данные заказа и код ответа 200.')
    def test_user_with_auth_can_get_order_success(self, user_creation_hard_data):
        token = user_creation_hard_data.json()['accessToken']
        response = requests.get(f'{data.URL}{data.ORDER_ENDPOINT}', headers={'Authorization': token},
                                data=data.USER_LOGIN)
        assert response.status_code == 200 and response.json()['success'] is True, \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')

    @allure.title('Проверка ручки /api/order. '
                  '1.неавторизованный пользователь не может получить свои заказы'
                  '2.запрос возвращает ошибку и код ответа 401.')
    def test_user_without_auth_cannot_get_order(self):
        response = requests.get(f'{data.URL}{data.ORDER_ENDPOINT}')
        assert response.status_code == 401 and data.ERROR_UNAUTHORIZED in response.json()['message'], \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')
