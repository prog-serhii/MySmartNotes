from __future__ import annotations

import abc

from text_ocr.domain.value_objects import Image


class InvalidImageFormat(Exception):
    pass


class ImageProcessingProvider(abc.ABC):
    _original_image: Image

    @property
    def image(self) -> Image:
        return self._return_image_buffer()

    @image.setter
    def image(self, img: Image) -> None:
        self._original_image = img

    @abc.abstractmethod
    def binarize(self) -> ImageProcessingProvider:
        pass

    @abc.abstractmethod
    def remove_noise(self) -> ImageProcessingProvider:
        pass

    @abc.abstractmethod
    def remove_borders(self) -> ImageProcessingProvider:
        pass

    @abc.abstractmethod
    def _return_image_buffer(self) -> Image:
        pass
