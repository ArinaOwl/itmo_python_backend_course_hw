from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_root():
    """
    Возвращает описание.

    :return: "Редактируемая тетрадь для записи иностранных слов"
    """
    return {"message": "Редактируемая тетрадь для записи иностранных слов"}
