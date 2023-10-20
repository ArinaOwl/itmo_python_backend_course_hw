from app.user.contracts import UserSignup

USERS = [
    UserSignup(
        username="iivanov",
        password="qwerty",
        name="Иван",
        surname="Иванов",
        email="i.ivanov@example.ru"
    ),
    UserSignup(
        username="ppetrov",
        password="1111",
        name="Петр",
        surname="Петров",
        email="p.petrov@example.ru"
    ),
]
