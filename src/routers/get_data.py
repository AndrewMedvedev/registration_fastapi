from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.classes import GetUserData

router_data = APIRouter(prefix="/api/v1/get", tags=["get_data"])


@router_data.get("data/{user_id}")
async def get_data(
    user_id: int,
) -> JSONResponse:
    return await GetUserData().get_data(user_id=user_id)
    


@router_data.get("number/{phone_number}")
async def get_number(
    phone_number: str,
) -> JSONResponse:
    return await GetUserData().get_number(phone_number=phone_number)

