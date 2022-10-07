import abc

from foundation.value_objects import Text
from text_ocr.domain.value_objects import Image


class TextRecognitionProvider(abc.ABC):

    @abc.abstractmethod
    def image_to_text(self, image: Image) -> Text:
        pass
