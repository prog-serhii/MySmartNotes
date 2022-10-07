import abc

from text_ocr.domain.value_objects import Image


class InvalidImageFormat(Exception):
    pass


class ImageProcessingProvider(abc.ABC):

    @abc.abstractmethod
    def open(self, image: Image) -> None:
        pass
