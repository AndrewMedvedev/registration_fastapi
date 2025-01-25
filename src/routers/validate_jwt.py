from fastapi import APIRouter
from src.classes.jwt_classes import ValidateJWT

router = APIRouter(prefix="/validate/jwt", tags=["validate/jwt"])


@router.get(
    "/refresh",
    response_model=None,
)
async def validate_refresh(
    refresh: str,
) -> str | bool:
    return await ValidateJWT(refresh).validate_refresh()


@router.get(
    "/access",
    response_model=None,
)
async def validate_access(
    access: str,
) -> dict | bool:
    return await ValidateJWT(access).validate_access()
