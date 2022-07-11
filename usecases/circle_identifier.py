from typing import Union

import cv2
import numpy as np
from models.circle_element import CircleElement


class CircleIdentifier:
    def __debug_circles(self, image: cv2.Mat, circles: tuple[CircleElement]) -> cv2.Mat:
        # Convert to colored image
        debugged_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        # Draw circles
        for circle in circles:
            cv2.circle(
                debugged_image,
                circle.center,
                circle.radius,
                (0, 255, 0),
                2,
            )
            cv2.circle(debugged_image, circle.center, 2, (0, 0, 255), 3)
        return debugged_image

    def execute(self, image: cv2.Mat) -> Union[tuple[CircleElement], cv2.Mat]:
        # Apply HoughCircles
        circles = cv2.HoughCircles(
            image,
            cv2.HOUGH_GRADIENT,
            1,
            8,
            param1=40,
            param2=19,
            minRadius=0,
            maxRadius=30,
        )

        identified_circles = []
        if circles is not None:
            for circle_data in np.uint16(np.around(circles[0, :])):
                identified_circles.append(CircleElement(circle_data))

        # return self.__debug_circles(image, circles)
        return tuple(identified_circles), self.__debug_circles(
            image, identified_circles
        )
