from app.user import contracts

USERS = [
    contracts.User(
        username="iivanov",
        password="qwerty",
        name="Иван",
        surname="Иванов",
        email="i.ivanov@example.ru"
    ),
    contracts.User(
        username="ppetrov",
        password="1111",
        name="Петр",
        surname="Петров",
        email="p.petrov@example.ru"
    ),
]
