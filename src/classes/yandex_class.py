import base64
import hashlib
import os
from fastapi.responses import JSONResponse

from src.classes.reuse_class import ReUse
from src.config import Settings
from src.database import get_data_user_yandex, get_token_user_yandex
from src.database.models import UserYandex
from src.database.schemas import (
    DictGetDataTokenYandex,
    DictGetDataYandex,
    DictLinkYandex,
)
from src.interfaces import OtherAuthorizationsBase
from src.services.orm import ORMService


class Yandex(OtherAuthorizationsBase):

    def __init__(self, code: str = None, access_token: str = None) -> None:
        self.code = code
        self.access_token = access_token
        self.settings = Settings
        self.reuse = ReUse
        self.user = UserYandex

    async def link(
        self,
    ) -> str:
        code_verifier = (
            base64.urlsafe_b64encode(os.urandom(128)).rstrip(b"=").decode("utf-8")
        )
        code_challenge = (
            base64.urlsafe_b64encode(
                hashlib.sha256(code_verifier.encode("utf-8")).digest()
            )
            .rstrip(b"=")
            .decode("utf-8")
        )
        return await self.reuse.link(
            setting=self.settings.YANDEX_AUTH_URL,
            dictlink=DictLinkYandex(code_challenge=code_challenge).model_dump(),
            code_verifier=code_verifier,
        )

    async def get_token(self, code_verifier: str) -> JSONResponse:
        return await self.reuse(
            func=get_token_user_yandex,
        ).get_token(
            dictgetdata=DictGetDataYandex(
                code=self.code, code_verifier=code_verifier
            ).model_dump(),
        )

    async def registration(self) -> JSONResponse:
        user = await get_data_user_yandex(
            DictGetDataTokenYandex(oauth_token=self.access_token).model_dump()
        )
        user_model = self.user(
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            id_yandex=user.get("id"),
            login=user.get("login"),
            email=user.get("default_email"),
        )
        return await self.reuse().registration(
            user_model=user_model,
        )

    async def login(self) -> JSONResponse:
        return await self.reuse(
            func=get_data_user_yandex,
        ).login(
            dictgetdatatoken=DictGetDataTokenYandex(
                oauth_token=self.access_token
            ).model_dump(),
            stmt_get=ORMService().get_user_email_yandex,
            field="default_email",
        )
