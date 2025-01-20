from fastapi import HTTPException, status
from src.database.models import UserVk
from src.classes.jwt_classes import JWTCreate
from src.services.orm import ORMService
from src.config import Settings as settings
from src.database.schemas import DictLink, DictGetData
from src.database.controls import get_data_user


class VK:

    def __init__(self, code: str = None) -> None:
        self.code = code

    async def vk_link(self) -> str:
        url = f"{settings.VK_AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in DictLink().model_dump().items()])}"
        return url

    async def vk_registration(self) -> dict:
        model = DictGetData(code=self.code).model_dump()
        user = await get_data_user(model)
        user_model = UserVk(
            id_vk=user.get("user_id"),
            email=user.get("email"),
        )
        await ORMService().add_user(user_model)
        data = {"user_name": user.get("email")}
        access = await JWTCreate(data).create_access()
        refresh = await JWTCreate(data).create_refresh()
        return {
            "access": access,
            "refresh": refresh,
        }

    async def vk_login(self) -> dict | HTTPException:
        model = DictGetData(code=self.code).model_dump()
        user = await get_data_user(model)
        stmt = await ORMService().get_user_email_vk(user.get("email"))
        print(user.get("email"))
        if stmt.email == user.get("email"):
            data = {"user_name": user.get("email")}
            access = await JWTCreate(data).create_access()
            refresh = await JWTCreate(data).create_refresh()
            return {
                "access": access,
                "refresh": refresh,
            }
        else:
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
