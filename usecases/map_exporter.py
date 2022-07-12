import numpy as np
from models.entities.map_data import BlockTypes, MapData
from repositories.file_saver_repository import FileSaverRepository
from utils.generators import output_filename


class MapExporter:
    def __init__(self, collision_groups: list = []):
        self.__collision_groups = collision_groups
        self.__map_size = (22, 19)

    def export_map(self, filename: str, output_folder: str, map: tuple) -> None:
        builder = ""
        for row in map:
            for block in row:
                builder += str(block)
            builder += "\n"

        saver_repo = FileSaverRepository()
        saver_repo.save_file(
            path=output_folder,
            filename=output_filename(filename) + ".txt",
            content=builder,
        )

    def export(self, map_data: MapData, output_path: str, input_name: str = "") -> None:
        map_destination = np.zeros(
            shape=(self.__map_size[0], self.__map_size[1]), dtype=np.uint8
        )
        for contour in map_data.walls.contours:
            for point_array in contour:
                point = point_array[0]
                height = (point[0] * self.__map_size[0]) / map_data.size[0]
                width = (point[1] * self.__map_size[1]) / map_data.size[1]

                current_block = map_destination[int(height), int(width)]
                match current_block:
                    case BlockTypes.POINTS.value:
                        map_destination[int(height), int(width)] = BlockTypes.AIR.value
                    case BlockTypes.AIR.value:
                        map_destination[
                            int(height), int(width)
                        ] = BlockTypes.GHOST_DOOR.value
                    case BlockTypes.GHOST_DOOR.value:
                        map_destination[int(height), int(width)] = BlockTypes.WALL.value
        print(map_destination)
        self.export_map(input_name, output_path, map_destination)
