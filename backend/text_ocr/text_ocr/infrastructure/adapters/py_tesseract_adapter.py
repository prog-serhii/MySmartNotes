import pytesseract

from foundation.value_objects import Text
from text_ocr.domain.value_objects import Image, ImageLanguage
from text_ocr.application.ports import TextRecognitionProvider


class PyTesseractAdapter(TextRecognitionProvider):

    def image_to_text(self, image: Image, language: ImageLanguage) -> Text:
        if language == ImageLanguage.AUTO:
            lang_config = None
        else:
            lang_config = language.value

        return pytesseract.image_to_string(image, lang=lang_config, config='--eom 3 --psm 1')
