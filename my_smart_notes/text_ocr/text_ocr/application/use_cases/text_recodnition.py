import abc
from dataclasses import dataclass

from text_ocr.domain.value_objects import Image, ImageLanguage


@dataclass
class TextRecognitionInputDto:
    screenshot: Image
    language: ImageLanguage


@dataclass
class TextRecognitionOutputDto:
    # TODO: foundation
    # text: NoteText
    text: str


class TextRecognitionOutputBoundary(abc.ABC):
    
    @abc.abstractclassmethod
    def present(self, output_dto: TextRecognitionOutputDto) -> None:
        pass


class TextRecognition:

    def __init__(self, output_boundary: TextRecognitionOutputBoundary) -> None:
        self._output_boundary = output_boundary
    
    def execute(self, input_dto: TextRecognitionInputDto) -> None:
        # TODO: text recognition
        output_dto = TextRecognitionOutputDto(text='Some text')
        self._output_boundary.present(output_dto)
