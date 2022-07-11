import cv2
from models.contours import Contours
from models.hsv_colors import HSVColors
from utils.cv_helpers import hsv_to_rgb


class LineIdentifier:
    def debug_contours(self, image: cv2.Mat, contours: list) -> cv2.Mat:
        image_with_contours = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        color_list = (
            HSVColors.BLUE,
            HSVColors.GREEN,
            HSVColors.YELLOW,
            HSVColors.MAGENTA,
            HSVColors.CYAN,
            HSVColors.PURPLE,
        )
        color_index = 0
        # paint the contours with red
        for contour in contours:
            if color_index >= len(color_list):
                color_index = 0
            image_with_contours = cv2.drawContours(
                image_with_contours,
                [contour],
                -1,
                hsv_to_rgb(color_list[color_index].value.max),
                2,
            )
            color_index += 1

        return image_with_contours

    def execute(self, image: cv2.Mat) -> Contours:
        contours, hierarchy = cv2.findContours(
            image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
        )
        # return self.__debug_contours(image, contours)
        return Contours(
            contours=contours, hierarchy=hierarchy, is_sorted=False
        ), self.debug_contours(image, contours)
