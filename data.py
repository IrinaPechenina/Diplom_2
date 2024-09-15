URL = 'https://stellarburgers.nomoreparties.site/'

USER_REGISTER_ENDPOINT = 'api/auth/register'  # Создание пользователя POST
USER_LOGIN_ENDPOINT = 'api/auth/login'  # Логин пользователя/авторизация POST
USER_DATA_CHANGE_ENDPOINT = 'api/auth/user'  # Изменение данных пользователя PATCH
ORDER_ENDPOINT = 'api/orders'  # Создание заказа  POST,  Получение заказов пользователя GET

RESPONSE_NAME = 'name'
ERROR_EMPTY_FIELD = 'Email, password and name are required fields'  # Если нет одного из полей status_code == 403
ERROR_UNAUTHORIZED = 'You should be authorised'  #
ERROR_EXISTED_USER = 'User already exists'  # status_code == 403
ERROR_USER_LOGIN_DATA = 'email or password are incorrect'  # status_code == 401
ERROR_NO_INGREDIENTS_IN_ORDER = 'Ingredient ids must be provided'

EXISTED_USER_DATA = {
    "email": "irina_pe@yandex.ru",
    "password": "Leto_2024_08",
    "name": "Irina_Pe"
}

USER_LOGIN = {
    "email": "irina_pe@yandex.ru",
    "password": "Leto_2024_08"
}

USER_LOGIN_WITH_ERROR = {
    "email": "@yandex.ru",
    "password": "11"
}

USER_LOGIN_EMPTY_EMAIL = {
    "email": "",
    "password": "Leto_2024_08"
}

USER_LOGIN_EMPTY_PASSWORD = {
    "email": "irina_pe@yandex.ru",
    "password": ""
}

USER_DATA_EMPTY_EMAIL = {
    "email": "",
    "password": "Leto_24",
    "name": "Irina_P"
}

USER_DATA_EMPTY_PASSWORD = {
    "email": "irina_p@yandex.ru",
    "password": "",
    "name": "Irina_P"
}

USER_DATA_EMPTY_NAME = {
    "email": "irina_p@yandex.ru",
    "password": "Leto_24",
    "name": ""
}

USER_NEW_EMAIL = {
    "email": "pe@yandex.ru",
    "password": "Leto_2024_08",
    "name": "Irina_Pe"
}

USER_NEW_PASSWORD = {
    "email": "irina_pe@yandex.ru",
    "password": "08",
    "name": "Irina_Pe"
}

USER_NEW_NAME = {
    "email": "irina_pe@yandex.ru",
    "password": "Leto_2024_08",
    "name": "Pe"
}

INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa6f"]}
ORDER_NAME = 'Бессмертный краторный бургер'
INGREDIENTS_WITH_ERROR = {"ingredients": ["61c0c5a71d1f82001bdaaa6c", "6"]}

UNIQUE_USER_DATA = {
    "email": "1r1nA_P6@ya.ru",
    "password": "Motto_098",
    "name": "Irinaaaaa"
}

