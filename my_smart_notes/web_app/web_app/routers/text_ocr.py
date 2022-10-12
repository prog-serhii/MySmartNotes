import io

from fastapi import APIRouter, UploadFile, File, Depends, Form
from dependency_injector.wiring import inject, Provide

from text_ocr import (
    TextRecognition, TextRecognitionOutputBoundary, TextRecognitionInputDto, TextRecognitionOutputDto, ImageLanguage
)
from main import ApplicationContainer


router = APIRouter()


@router.post('/text_ocr/')
@inject
async def text_ocr(
    file: UploadFile = File(...),
    language: ImageLanguage = Form(),
    text_recognition_uc: TextRecognition = Depends(Provide[ApplicationContainer.text_ocr_package.text_recognition_uc]),
    presenter: TextRecognitionOutputBoundary = Depends(
        Provide[ApplicationContainer.text_ocr_package.text_recognition_output_boundary]
    )
):
    bytes_str = io.BytesIO(await file.read())
    input_dto = TextRecognitionInputDto(bytes_str, language)

    text_recognition_uc.execute(input_dto)
    return presenter.response  # type: ignore
