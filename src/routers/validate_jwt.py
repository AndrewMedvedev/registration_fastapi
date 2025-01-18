from fastapi import APIRouter
from src.classes.jwt_classes import JWTCreate, ValidateJWT

router = APIRouter(prefix="/validate/jwt", tags=["validate/jwt"])


@router.post("/refresh")
async def validate_refresh(
    refresh: str,
) -> dict | bool:
    tkn_refresh = await ValidateJWT(refresh).validate_refresh()
    if tkn_refresh != False:
        data = {"user_name": tkn_refresh}
        access = await JWTCreate(data).create_access()
        return {"access": access}
    else:
        False


@router.get("/access")
async def validate_access(
    access: str,
) -> bool:
    tkn_access = await ValidateJWT(access).validate_access()
    if tkn_access != False:
        return True
    else:
        False
