from fastapi.responses import JSONResponse

from src.classes.jwt_classes import JWTCreate
from src.config import Settings as settings
from src.database import get_data_user_vk, get_token_user_vk
from src.database.models import UserVk
from src.database.schemas import DictGetDataTokenVK, DictGetDataVK, DictLinkVK
from src.services.orm import ORMService


class VK:

    def __init__(
        self, code: str = None, device_id: str = None, access_token: str = None
    ) -> None:
        self.code = code
        self.device_id = device_id
        self.access_token = access_token

    async def vk_link() -> str:
        url = f"{settings.VK_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in DictLinkVK().model_dump().items()])}"
        return url

    async def vk_get_token(self) -> JSONResponse:
        model = DictGetDataVK(code=self.code, device_id=self.device_id).model_dump()
        user = await get_token_user_vk(model)
        return JSONResponse(content=user)

    async def vk_registration(self) -> JSONResponse:
        model = DictGetDataTokenVK(access_token=self.access_token).model_dump()
        user = await get_data_user_vk(model)
        user_model = UserVk(
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            id_vk=int(user.get("user_id")),
            email=user.get("email").lower(),
        )
        user_id = await ORMService().add_user(user_model)
        data = {"user_id": user_id}
        access = await JWTCreate(data).create_access()
        refresh = await JWTCreate(data).create_refresh()
        return JSONResponse(
            content={
                "access": access,
                "refresh": refresh,
            }
        )

    async def vk_login(self) -> JSONResponse:
        model = DictGetDataTokenVK(access_token=self.access_token).model_dump()
        user = await get_data_user_vk(model)
        stmt = await ORMService().get_user_email_vk(user.get("email").lower())
        if stmt.email == user.get("email").lower():
            data = {"user_id": stmt.id}
            access = await JWTCreate(data).create_access()
            refresh = await JWTCreate(data).create_refresh()
            return JSONResponse(
                content={
                    "access": access,
                    "refresh": refresh,
                }
            )
