from models.circle_element import CircleElement
from models.contours import Contours


class MapData:
    def __init__(self, walls: Contours, spawners: CircleElement) -> None:
        self.walls: Contours = walls
        self.spawners: CircleElement = spawners
