import cv2
from models.hsv_colors import HSVColors
from repositories import ImageRepositoryProvider
from usecases.circle_identifier import CircleIdentifier
from usecases.color_splitter import ColorSpliter
from usecases.line_identifier import LineIdentifier
from usecases.map_exporter import MapExporter
from usecases.threshold_applier import ThresholdApplier
from utils.generators import output_filename


class ParseImage(ImageRepositoryProvider):
    def __init__(self, exporter: MapExporter, dimensions: tuple[int, int]) -> None:
        self.__exporter = exporter
        self.__dimensions = dimensions
        super().__init__()

    def export_image(self, input_name: str, output_folder: str, image: cv2.Mat) -> None:
        self._image_exporter.save(
            output_folder,
            output_filename(input_name) + ".png",
            image,
        )

    def _execute(self, image: cv2.Mat) -> None:
        threshould_applier = ThresholdApplier(threshold=(230, 255))
        line_identifier = LineIdentifier()
        circle_indetifier = CircleIdentifier()
        threshould_image = threshould_applier.apply_threshould(image)
        contours, debug_image = line_identifier.execute(threshould_image)
        spawners, _ = circle_indetifier.execute(threshould_image)

        # Circle removed from the contours
        return debug_image

    def parse(self, image_src: str, output: str) -> None:
        image = self._image_loader.load(image_src)

        # Resize the image to the desired size
        image = cv2.resize(
            src=image, dsize=(int(self.__dimensions[0]), int(self.__dimensions[1]))
        )

        splitter = ColorSpliter(
            colors=(HSVColors.BLUE, HSVColors.GREEN, HSVColors.YELLOW)
        )
        image_sections = splitter.execute(image)

        for section in image_sections.values():
            self.export_image(image=section, output_folder=output, input_name=image_src)

        debug_image = self._execute(image)
        self.export_image(image=debug_image, output_folder=output, input_name=image_src)
