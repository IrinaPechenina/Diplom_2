import allure
import pytest
import requests
import data


class TestUserRegister:
    @allure.title('Проверка ручки /api/auth/register. '
                  '1.можно создать уникального пользователя, передав в ручку все обязательные поля'                  
                  '2.успешный запрос возвращает данные пользователя, код ответа 200.')
    def test_create_unique_user_success(self, user_creation):
        assert user_creation.status_code == 200 and data.RESPONSE_NAME in user_creation.json()['user'], \
            f'status code{user_creation.status_code}, text={user_creation.text}'
        print(f'{user_creation.status_code}, {user_creation.json()}')

    @allure.title('Проверка ручки /api/auth/register. '
                  '1.нелья создать пользователя, который уже зарегистрирован'
                  '2.запрос возвращает ошибку, код ответа 403')
    def test_create_user_with_existed_login_false(self, user_creation_hard_data):
        response = requests.post(f'{data.URL}{data.USER_REGISTER_ENDPOINT}', data=data.EXISTED_USER_DATA)
        expected_result = data.ERROR_EXISTED_USER
        assert response.status_code == 403 and expected_result in response.json()['message'], \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')

    @allure.title('Проверка ручки /api/auth/register. '
                  '1.нелья создать пользователя, если не заполнить одно из обязательных полей (email, пароль, имя)'
                  '2.запрос возвращает ошибку, код ответа 403')
    @pytest.mark.parametrize('user_data', [
        data.USER_DATA_EMPTY_EMAIL,
        data.USER_DATA_EMPTY_PASSWORD,
        data.USER_DATA_EMPTY_NAME
    ])
    def test_create_user_without_required_data_false(self, user_data):
        response = requests.post(f'{data.URL}{data.USER_REGISTER_ENDPOINT}', data=user_data)
        result = data.ERROR_EMPTY_FIELD
        assert response.status_code == 403 and result in response.json()['message'], \
            f'status code{response.status_code}, text={response.text}'
        print(f'{response.status_code}, {response.json()}')
