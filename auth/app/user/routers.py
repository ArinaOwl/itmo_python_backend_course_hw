from typing import Union

from fastapi import APIRouter

from app.user.contracts import UserSignup, UserLogin
from app.user.constants import USERS

router = APIRouter(prefix="/users")


@router.get("/")
async def read_users():
    """
    Вывод списка зарегистрированных в системе пользователей.
    :return: список зарегистрированных пользователей
    """
    users_list = []
    for user in USERS:
        users_list.append({
            "username": user.username,
            "name": user.name,
            "surname": user.surname
        })
    return users_list


@router.post("/signup")
def signup(user_data: UserSignup):
    """
    Регистрация нового пользователя.
    В текущей версии введенные данные не сохраняются.
    param user_data: данные пользователя
    :return: словарь данных нового пользователя
    """
    return user_data.model_dump()


@router.post("/login")
def login(user_data: UserLogin):
    """
    Вход зарегистрированного в системе пользователя.
    В текущей версии обработка не производится.
    param user_data: данные пользователя
    :return: имя в системе и пароль пользователя
    """
    return {"username": user_data.username, "password": user_data.password}


@router.get("/{username}")
async def read_user(username: str):
    """
    Вывод данных пользователя по имени пользователя в системе.
    :param username: имя пользователя
    :return: данные пользователя
    """
    users_dict = {user.username: {
        "name": user.name,
        "surname": user.surname,
        "email": user.email
    } for user in USERS}

    if username in users_dict:
        return users_dict[username]
    else:
        return "User with this username is not registered"
