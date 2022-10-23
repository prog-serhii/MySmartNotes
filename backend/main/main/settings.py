from pydantic import BaseSettings


class Settings(BaseSettings):

    # text_ocr_package_overriders: dict = {
    #     'text_recognition_output_boundary': {
    #         'class': 'web_app.presenters.TextRecognitionPresenter',
    #         'provider_class': 'Singleton'
    #     }
    # }

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
