from fastapi import Body, APIRouter
from typing import Annotated
from src.application.modules.user.dto.requests.create_user_request import (
    SCreateUserRequest,
)
from src.application.modules.user.dto.responses.create_user_response import (
    SCreateUserResponse,
)
from src.application.modules.user.use_cases.create_user_use_case import (
    ICreateUserUseCase,
)
from dishka import FromDishka

user_router: APIRouter = APIRouter(prefix="/users/api/v1", tags=["Users"])


@user_router.post("/", response_model=SCreateUserResponse)
async def create_user(
    request: Annotated[SCreateUserRequest, Body()],
    use_case: FromDishka[ICreateUserUseCase],
) -> SCreateUserResponse:
    return await use_case.execute(request=request)
