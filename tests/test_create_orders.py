import allure
import requests
import data


class TestCreateOrders:
    @allure.title('Проверка ручки api/orders. '
                  '1.авторизованный пользователь может создать заказ, указав ингредиенты'                  
                  '2.успешный запрос возвращает данные заказа, код ответа 200.')
    def test_create_order_by_user_with_auth_success(self, user_creation_hard_data):
        ingredients_data = data.INGREDIENTS
        token = user_creation_hard_data.json()['accessToken']
        response = requests.post(f'{data.URL}{data.ORDER_ENDPOINT}', headers={'Authorization': token},
                                 data=ingredients_data)
        assert response.status_code == 200 and response.json()['name'] == data.ORDER_NAME,\
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')

    @allure.title('Проверка ручки api/orders. '
                  '1.авторизованный пользователь не может создать заказ, не указав ингредиенты'                  
                  '2.запрос возвращает ошибку, код ответа 400.')
    def test_user_with_auth_cannot_create_order_without_ingrt(self, user_creation_hard_data):
        ingredients_data = None
        token = user_creation_hard_data.json()['accessToken']
        response = requests.post(f'{data.URL}{data.ORDER_ENDPOINT}', headers={'Authorization': token},
                                 data=ingredients_data)
        expected_result = data.ERROR_NO_INGREDIENTS_IN_ORDER
        assert response.status_code == 400 and expected_result in response.json()['message'], \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')

    @allure.title('Проверка ручки api/orders. '
                  '1.авторизованный пользователь не может создать заказ, если указан невалидный хеш ингредиента'                  
                  '2.запрос возвращает ошибку, код ответа 500.')
    def test_user_with_auth_cannot_create_order_ingrt_with_error(self, user_creation_hard_data):
        ingredients_data = data.INGREDIENTS_WITH_ERROR
        token = user_creation_hard_data.json()['accessToken']
        response = requests.post(f'{data.URL}{data.ORDER_ENDPOINT}', headers={'Authorization': token},
                                 data=ingredients_data)
        assert response.status_code == 500
        print(f'{response.status_code}')

    @allure.title('Проверка ручки api/orders. '
                  '1.неавторизованный пользователь может создать заказ, указав ингредиенты'                  
                  '2. запрос возвращает данные заказа, код ответа 200.')
    def test_create_order_by_user_without_auth(self):
        ingredients_data = data.INGREDIENTS
        response = requests.post(f'{data.URL}{data.ORDER_ENDPOINT}', data=ingredients_data)
        assert response.status_code == 200 and response.json()['name'] == data.ORDER_NAME, \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')
