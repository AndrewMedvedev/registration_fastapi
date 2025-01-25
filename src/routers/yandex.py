from fastapi import APIRouter, HTTPException, status
from src.classes.yandex_class import Yandex

router = APIRouter(prefix="/yandex", tags=["yandex"])


@router.get(
    "/link",
    response_model=None,
)
async def yandex_link() -> str | HTTPException:
    try:
        return await Yandex.yandex_link()
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get(
    "/get/token",
    response_model=None,
)
async def yandex_get_token(code: str) -> str | HTTPException:
    try:
        return await Yandex(code=code).yandex_get_token()
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get(
    "/registration",
    response_model=None,
)
async def yandex_registration(access_token: str) -> dict | HTTPException:
    try:
        return await Yandex(access_token=access_token).yandex_registration()
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get(
    "/login",
    response_model=None,
)
async def yandex_login(access_token: str) -> dict | HTTPException:
    try:
        return await Yandex(access_token=access_token).yandex_login()
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
