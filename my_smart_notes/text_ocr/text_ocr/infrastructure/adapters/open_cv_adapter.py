import io

import cv2
import numpy as np

from text_ocr import Image
from text_ocr.application.ports import ImageProcessingProvider, InvalidImageFormat


class OpenCVAdapter(ImageProcessingProvider):

    def open_image_buffer(self, image: Image) -> ImageLibFormat:
        try:
            return cv2.imdecode(np.frombuffer(image.getbuffer(), np.uint8), -1)
        # TODO:
        except:
            raise InvalidImageFormat

    def binarize(self, image: ImageLibFormat) -> ImageLibFormat:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, im_bw = cv2.threshold(gray_image, 200, 230, cv2.THRESH_TOZERO)
        return im_bw

    def remove_noise(self, image: ImageLibFormat) -> ImageLibFormat:
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(image, 2)
        return image

    def remove_borders(self, image: ImageLibFormat) -> ImageLibFormat:
        contours, heiarchyy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnt_sorted = sorted(contours, key=lambda contour: cv2.contoursArea(contour))
        cnt = cnt_sorted[-1]
        x, y, w, h = cv2.bpundingRect(cnt)
        return image[y:y + h, x:x + w]

    def return_image_buffer(self, image: ImageLibFormat) -> Image:
        _, im_buf_arr = cv2.imencode('.png', image)
        return io.BytesIO(im_buf_arr)
