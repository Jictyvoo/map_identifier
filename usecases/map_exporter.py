from typing import Any

from models.contours import Contours


class MapExporter:
    def __init__(self, collision_groups: list):
        self.__collision_groups = collision_groups
        self.__block_size = (32, 32)

    def export(self, map_data: tuple[Contours], output_path: str):
        pass
