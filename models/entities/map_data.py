from enum import Enum

from models.circle_element import CircleElement
from models.contours import Contours


class BlockTypes(Enum):
    AIR = 2
    POINTS = 0
    WALL = 1
    GHOST_DOOR = 3


class MapData:
    def __init__(
        self, walls: Contours, spawners: CircleElement, size: tuple[int, int]
    ) -> None:
        self.walls: Contours = walls
        self.spawners: CircleElement = spawners
        self.size: tuple[int, int] = size
