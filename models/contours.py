import cv2

from models.circle_element import CircleElement


class Contours:
    def __init__(self, contours: tuple, hierarchy: any, is_sorted: bool) -> None:
        self.contours = contours
        self.hiearchy = hierarchy
        self._is_sorted = is_sorted

    def __sort_contours(self) -> None:
        if not self._is_sorted:
            self.contours = sorted(
                self.contours,
                key=lambda element: cv2.contourArea(element, False),
                reverse=True,
            )

    @property
    def biggest(self) -> tuple:
        self.__sort_contours()
        return self.contours[0]

    @property
    def smallest(self) -> tuple:
        smallest_area = cv2.contourArea(self.contours[0], False)
        element_index = 0
        for index in range(len(self.contours)):
            contour = self.contours[index]
            area = cv2.contourArea(contour, False)
            if area > 1 and area < smallest_area:
                smallest_area = area
                element_index = index

        return self.contours[element_index]

    def check_contour_inside_circle(
        self, circle_element: CircleElement, contour: tuple
    ) -> bool:

        return cv2.pointPolygonTest(contour, circle_element.center, False) == 1

    def remove_contours(self, contours: list, is_circle: bool = False) -> None:
        if is_circle:
            sub_contours = []
            for circle_element in contours:
                for internal_contour in self.contours:
                    if self.check_contour_inside_circle(
                        circle_element=circle_element, contour=internal_contour
                    ):
                        sub_contours.append(internal_contour)
            return sub_contours
