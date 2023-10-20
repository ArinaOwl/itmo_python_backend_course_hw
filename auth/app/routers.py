from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    """
    Возвращает "Hello world"
    :return: "Hello World"
    """
    return "Hello World"
