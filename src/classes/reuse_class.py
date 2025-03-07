from fastapi.responses import JSONResponse

from src.classes.jwt_classes import JWTCreate
from src.interfaces import ReUseBase
from src.services.orm import ORMService


class ReUse(ReUseBase):

    def __init__(self, func=None):
        self.func = func
        self.orm = ORMService()
        self.jwt_create = JWTCreate

    @staticmethod
    async def link(setting: str, dictlink: dict, code_verifier: str) -> dict:
        url = f"{setting}?{'&'.join([f'{k}={v}' for k, v in dictlink.items()])}"
        return {"url": url, "code_verifier": code_verifier}

    async def get_token(self, dictgetdata: dict) -> JSONResponse:
        return JSONResponse(content=await self.func(dictgetdata))

    async def registration(self, user_model) -> JSONResponse:
        await self.orm.add_user(user_model)
        return JSONResponse(content={"message": 200})

    async def login(
        self,
        dictgetdatatoken: dict,
        stmt_get,
        field: str,
    ) -> JSONResponse:
        user = await self.func(dictgetdatatoken)
        stmt = await stmt_get(user.get(field).lower())
        if stmt.email == user.get(field).lower():
            data = {"user_id": stmt.user_id}
            access = await self.jwt_create(data).create_access()
            refresh = await self.jwt_create(data).create_refresh()
            return JSONResponse(
                content={
                    "access": access,
                    "refresh": refresh,
                }
            )
