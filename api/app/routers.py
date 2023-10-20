from fastapi import APIRouter
from aiohttp import ClientSession
from app.contracts import UserSignup, UserLogin, UserUpdateDictRequest
import os

router = APIRouter()


@router.get("/")
def read_root():
    """
    Возвращает "Hello world"
    :return: "Hello World"
    """
    return "Hello World"


@router.post("/signup")
async def signup(user_data: UserSignup):
    """
    Регистрация нового пользователя

    param user_data: данные для создания пользователя
    return: ответ сервера аутентификации
    """
    async with ClientSession() as session:
        async with session.post(
                f"{os.getenv('AUTH_IP', 'http://127.0.0.1:8001')}/users/signup",
                json=user_data.model_dump(),
        ) as resp:
            response = await resp.json()
        print(user_data.model_dump())
    return response


@router.post("/login")
async def login(user_data: UserLogin):
    """
    Авторизация пользователя

    param user_data: данные для входа
    return: ответ сервера аутентификации
    """
    async with ClientSession() as session:
        async with session.post(
                f"{os.getenv('AUTH_IP', 'http://127.0.0.1:8001')}/users/login",
                json=user_data.model_dump(),
        ) as resp:
            response = await resp.json()

    return response


@router.post("/update_dictionary")
async def update_dict(user_data: UserUpdateDictRequest):
    """
    Изменение данных словаря (удаление или добавление слов)

    param user_data: данные для изменения словаря
    return: ответ сервера словаря
    """
    async with ClientSession() as session:
        if user_data.action_type == "remove":
            async with session.delete(
                    f"{os.getenv('DICT_IP', 'http://127.0.0.1:8002')}/words/{user_data.word}",
            ) as resp:
                response = await resp.json()
        elif user_data.action_type == "add":
            async with session.post(
                    f"{os.getenv('DICT_IP', 'http://127.0.0.1:8002')}/words/{user_data.word}"
                    f"?translation={user_data.translation}",
            ) as resp:
                response = await resp.json()
    return response


@router.get("/read_dictionary/{word}")
async def read_dict(word: str | None = None):
    """
    Чтение слов из словаря

    param word: слово
    return: ответ сервера словаря
    """
    word = "" if word is None else f"/{word}"
    async with ClientSession() as session:
        async with session.get(
                f"{os.getenv('DICT_IP', 'http://127.0.0.1:8002')}/words{word}",
        ) as resp:
            response = await resp.json()
    return response
