from fastapi import APIRouter

from src.classes.vk_class import VK
from src.database.schemas import RegistrationVK
from src.responses import CustomResponse

router_vk = APIRouter(prefix="/api/v1/vk", tags=["vk"])


@router_vk.get(
    "/link",
    response_model=None,
)
async def vk_link() -> CustomResponse:
    return await VK().link()


@router_vk.get(
    "/get/token/{code}/{device_id}/{code_verifier}",
    response_model=None,
)
async def vk_get_token(
    code: str,
    device_id: str,
    code_verifier: str,
) -> CustomResponse:
    return await VK().get_token(
        code=code,
        device_id=device_id,
        code_verifier=code_verifier,
    )


@router_vk.post(
    "/registration/",
    response_model=RegistrationVK,
)
async def vk_registration(model: RegistrationVK) -> CustomResponse:
    return await VK().registration(model=model)


@router_vk.post(
    "/login/{access_token}",
    response_model=None,
)
async def vk_login(access_token: str) -> CustomResponse:
    return await VK().login(access_token=access_token)
