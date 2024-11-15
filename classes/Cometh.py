from classes.SpaceObject import SpaceObject
from constants import COMETH_DIRECTIONS

class Cometh(SpaceObject):

    def __init__(self, row: int, column: int, direction: str):
        super().__init__(row, column);

        if not (direction.lower() in COMETH_DIRECTIONS):
            raise ValueError("Direction has to be one of the following: " + str(COMETH_DIRECTIONS));
        
        self.direction = direction;