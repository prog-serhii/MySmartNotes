from dependency_injector import containers, providers

from main.settings import Settings
from text_ocr import TextOcrContainer


__all__ = [
    'bootstrap_app'
]


class ApplicationContainer(containers.DeclarativeContainer):

    config = providers.Configuration(pydantic_settings=[Settings()])

    text_ocr = providers.Container(TextOcrContainer)


def bootstrap_app():
    """
    This is bootstrap function independent from the context.
    This should be used for Web, CLI, or worker context.
    """

    container = ApplicationContainer()
    container.wire(modules=[__name__])
