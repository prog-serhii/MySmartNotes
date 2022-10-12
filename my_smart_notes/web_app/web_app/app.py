from fastapi import FastAPI

from main import ApplicationContainer
from web_app.routers import text_ocr as text_ocr_api


ROUTERS = [text_ocr_api.router]


def create_app() -> FastAPI:
    container = ApplicationContainer()

    container.wire(modules=[text_ocr_api])

    app = FastAPI()
    app.container = container

    for router in ROUTERS:
        app.include_router(router)

    return app


app = create_app()
