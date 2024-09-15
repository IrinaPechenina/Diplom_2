import allure
import pytest
import requests
import data


class TestUserChange:
    @allure.title('Проверка ручки api/auth/user. '
                  '1.авторизованный пользователь может изменить свои данные, передав в ручку все обязательные поля '                  
                  '2.успешный запрос возвращает обновленные данные пользователя, код ответа 200.')
    @pytest.mark.parametrize('user_data', [
        data.USER_NEW_EMAIL,
        data.USER_NEW_PASSWORD,
        data.USER_NEW_NAME
    ])
    def test_change_user_data_with_auth_success(self, user_creation_hard_data, user_data):
        token = user_creation_hard_data.json()['accessToken']
        response = requests.patch(f'{data.URL}{data.USER_DATA_CHANGE_ENDPOINT}', headers={'Authorization': token},
                                  data=user_data)
        assert response.status_code == 200 and response.json()['success'] is True, \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')

    @allure.title('Проверка ручки api/auth/user. '
                  '1.неавторизованный пользователь не может изменить свои данные'                  
                  '2.запрос возвращает ошибку, код ответа 401.')
    @pytest.mark.parametrize('user_data', [
        data.USER_NEW_EMAIL,
        data.USER_NEW_PASSWORD,
        data.USER_NEW_NAME
    ])
    def test_change_user_data_without_auth_false(self, user_creation_hard_data, user_data):
        response = requests.patch(f'{data.URL}{data.USER_DATA_CHANGE_ENDPOINT}',
                                  data=user_data)
        expected_result = data.ERROR_UNAUTHORIZED
        assert response.status_code == 401 and expected_result in response.json()['message'], \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')
