import injector

from text_ocr import TextOcr


def _setup_dependency_injection() -> injector.Injector:
    return injector.Injector(
        [TextOcr()], auto_bind=False
    )
