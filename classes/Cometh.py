from classes.SpaceObject import SpaceObject

class Cometh(SpaceObject):

    directions = ["up", "down", "left", "right"];

    def __init__(self, row, column, direction):
        super().__init__(row, column)
        self.direction = direction;