import abc
from dataclasses import dataclass

from text_ocr.domain.value_objects import Image, ImageLanguage
from text_ocr.application.ports import ImageProcessingProvider, TextRecognitionProvider


@dataclass
class TextRecognitionInputDto:
    image: Image
    language: ImageLanguage


@dataclass
class TextRecognitionOutputDto:
    text: str


class TextRecognitionOutputBoundary(abc.ABC):
    
    @abc.abstractmethod
    def present(self, output_dto: TextRecognitionOutputDto) -> None:
        pass


class TextRecognition:

    def __init__(
        self,
        output_boundary: TextRecognitionOutputBoundary,
        image_processing_provider: ImageProcessingProvider,
        text_recognition_provider: TextRecognitionProvider
    ) -> None:
        self._output_boundary = output_boundary
        self._image_procession_provider = image_processing_provider
        self._text_recognition_rovider = text_recognition_provider
    
    def execute(self, input_dto: TextRecognitionInputDto) -> None:

        self._image_procession_provider.open_imagz(input_dto.image).binarize().remove_noise().remove_borders()

        text = self._text_recognition_rovider.image_to_text(self._image_procession_provider.image, input_dto.language)

        output_dto = TextRecognitionOutputDto(text=text)
        self._output_boundary.present(output_dto)
