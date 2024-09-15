import allure
import pytest
import requests
import data


class TestUserLogin:
    @allure.title('Проверка ручки /api/auth/login. '
                  '1.логин под существующим пользователем,'
                  '2.успешный запрос возвращает код ответа 200.')
    def test_existed_user_login_success(self, user_creation_hard_data):
        token = user_creation_hard_data.json()['accessToken']
        login = requests.post(f'{data.URL}{data.USER_LOGIN_ENDPOINT}', headers={'Authorization': token},
                              data=data.USER_LOGIN)
        assert login.status_code == 200 and login.json()['success'] is True, \
            f'status code{login.status_code}, text={login.text}'
        print(f'{login.status_code}, {login.json()['success']}')

    @allure.title('Проверка ручки /api/auth/login. '
                  'Если логин или пароль неверные или нет одного из полей,'
                  'запрос возвращает ошибку, код ответа 401.')
    @pytest.mark.parametrize('user_data', [
        data.USER_LOGIN_WITH_ERROR,
        data.USER_LOGIN_EMPTY_EMAIL,
        data.USER_LOGIN_EMPTY_PASSWORD
    ])
    def test_user_login_without_required_data_false(self, user_creation_hard_data, user_data):
        token = user_creation_hard_data.json()['accessToken']
        login = requests.post(f'{data.URL}{data.USER_LOGIN_ENDPOINT}', headers={'Authorization': token},
                              data=user_data)
        assert login.status_code == 401 and login.json()['message'] == data.ERROR_USER_LOGIN_DATA, \
            f'status code{login.status_code}, text={login.text}'
        print(f'{login.status_code}, {login.json()}')
