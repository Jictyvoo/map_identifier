import cv2
import numpy as np
from models.hsv_colors import HSVColor, HSVColors
from utils.cv_helpers import fill_holes


class ColorSpliter:
    """
    Takes an image and splits it into a list of images based on the color of the pixel.
    It uses the HSV color range to determine how to split the image.
    """

    def __init__(self, colors: tuple[HSVColors]) -> None:
        self.__color_thresholds = colors

    def __split_color(self, color_range: HSVColor, image: cv2.Mat) -> cv2.Mat:
        frame_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # show only the color in the range
        lower_color = np.array(color_range.min)
        upper_color = np.array(color_range.max)
        mask = cv2.inRange(frame_hsv, lower_color, upper_color)

        # show the result
        result = cv2.bitwise_and(image, image, mask=fill_holes(mask))

        return result

    def execute(self, image: cv2.Mat) -> dict[str, cv2.Mat]:
        """
        Splits the image into a list of images based on the color of the pixel.
        It uses the HSV color range to determine how to split the image.
        """
        all_subimages = {}
        for color in self.__color_thresholds:
            all_subimages[color.name] = self.__split_color(
                image=image, color_range=color.value
            )
        return all_subimages
