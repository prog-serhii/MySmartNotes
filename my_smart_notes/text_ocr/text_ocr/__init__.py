from dependency_injector import containers, providers

from text_ocr.application.use_cases import (
    TextRecognition,
    TextRecognitionInputDto,
    TextRecognitionOutputBoundary,
    TextRecognitionOutputDto
)
from text_ocr.domain.value_objects import (
    Image,
    ImageLanguage
)

__all__ = [
    # container
    'TextOCRContainer',
    # value objects
    'Image',
    'ImageLanguage',
    # use cases
    'TextRecognition',
    'TextRecognitionOutputBoundary',
    # input dtos
    'TextRecognitionInputDto',
    # output dtos
    'TextRecognitionOutputDto'
]


class TextOCRContainer(containers.DeclarativeContainer):

    text_recognition_output_boundary = providers.Dependency(instance_of=TextRecognitionOutputBoundary)
    text_recognition_uc = providers.Singleton(
        TextRecognition,
        output_boundary=text_recognition_output_boundary
    )
