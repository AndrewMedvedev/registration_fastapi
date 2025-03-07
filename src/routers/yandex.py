from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.classes.yandex_class import Yandex
from src.database.schemas import RegistrationYandex

router_yandex = APIRouter(prefix="/api/v1/yandex", tags=["yandex"])


@router_yandex.get(
    "/link",
    response_model=None,
)
async def yandex_link() -> str | JSONResponse:
    try:
        return await Yandex().link()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


@router_yandex.get(
    "/get/token/{code}/{code_verifier}",
    response_model=None,
)
async def yandex_get_token(code: str, code_verifier: str) -> JSONResponse:
    try:
        return await Yandex(code=code).get_token(code_verifier=code_verifier)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


@router_yandex.post(
    "/registration/",
    response_model=RegistrationYandex,
)
async def yandex_registration(model: RegistrationYandex) -> JSONResponse:
    try:
        return await Yandex().registration(model=model)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


@router_yandex.post(
    "/login/{access_token}",
    response_model=None,
)
async def yandex_login(access_token: str) -> JSONResponse:
    try:
        return await Yandex(access_token=access_token).login()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )
