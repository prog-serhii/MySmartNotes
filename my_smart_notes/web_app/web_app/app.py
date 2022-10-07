import injector
from fastapi import FastAPI

from web_app.routers.text_ocr import router as text_ocr_router


app = FastAPI()

app.include_router(text_ocr_router)
