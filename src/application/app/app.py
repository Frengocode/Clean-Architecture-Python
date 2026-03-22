from fastapi import FastAPI
from dishka import make_async_container, AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from src.application.common.shared.provider import SharedProvider
from src.application.modules.user.provider import UserProvider
from src.application.modules.user.controllers.api.v1.user import user_router
from src.application.common.shared.config.config import settings

container: AsyncContainer = make_async_container(SharedProvider(), UserProvider())


def get_app() -> FastAPI:
    app: FastAPI = FastAPI(title=settings.App.TITLE)

    app.include_router(user_router)
    setup_dishka(container=container, app=app)
    return app


app: FastAPI = get_app()
