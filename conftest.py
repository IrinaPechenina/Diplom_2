import pytest
import requests
import data


@pytest.fixture()  # уникальный пользователь
def user_creation():
    create_user = requests.post(f'{data.URL}{data.USER_REGISTER_ENDPOINT}', data=data.UNIQUE_USER_DATA)
    yield create_user
    token = create_user.json()['accessToken']
    requests.delete(f'{data.URL}{data.USER_DATA_CHANGE_ENDPOINT}', headers={'Authorization': token})


@pytest.fixture()
def user_creation_hard_data():
    create_user = requests.post(f'{data.URL}{data.USER_REGISTER_ENDPOINT}', data=data.EXISTED_USER_DATA)
    yield create_user
    token = create_user.json()['accessToken']
    requests.delete(f'{data.URL}{data.USER_DATA_CHANGE_ENDPOINT}', headers={'Authorization': token})
