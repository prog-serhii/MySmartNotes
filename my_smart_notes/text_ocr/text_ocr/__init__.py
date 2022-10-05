import injector

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
    # module
    'TextOCR',
    # value objects
    'Image',
    'ImageLanguage',
    # use cases
    'TextRecognition',
    'TextRecognitionOutputBoundary'
    # input dtos
    'TextRecognitionInputDto',
    # output dtos
    'TextRecognitionOutputDto'
]

class TextOCR(injector.Module):

    @injector.provider
    def text_recognition_uc(self, boundary: TextRecognitionOutputBoundary) -> TextRecognition:
        return TextRecognition(boundary)
