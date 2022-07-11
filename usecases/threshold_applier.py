import cv2


class ThresholdApplier:
    def __init__(self, threshold: tuple[int, int]) -> None:
        self.__threshold = threshold

    def apply_threshould(self, image: cv2.Mat) -> cv2.Mat:
        image_as_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(
            image_as_gray, self.__threshold[0], self.__threshold[1], cv2.THRESH_BINARY
        )

        return thresh
