from text_ocr import TextRecognitionOutputBoundary, TextRecognitionOutputDto


class TextRecognitionPresenter(TextRecognitionOutputBoundary):
    response: dict

    def present(self, output_dto: TextRecognitionOutputDto) -> None:
        self.response = {'response': output_dto.text}
