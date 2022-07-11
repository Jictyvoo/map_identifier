class CircleElement:
    def __init__(self, circle_list: tuple):
        self.center = (circle_list[0], circle_list[1])
        self.radius: float = circle_list[2]

    def __str__(self):
        return "CircleElement(center=%s, radius=%.2f)" % (self.center, self.radius)

    def __repr__(self) -> str:
        return self.__str__()
