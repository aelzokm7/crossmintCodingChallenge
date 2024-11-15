from classes.SpaceObject import SpaceObject
from constants.constants import COMETH_DIRECTIONS


class Cometh(SpaceObject):

    def __init__(self, row: int | str, column: int | str, direction: str):
        super().__init__(row, column);

        direction = direction.lower()

        if not (direction in COMETH_DIRECTIONS):
            raise ValueError("Direction Has To Be One Of The Following: " + str(COMETH_DIRECTIONS));
        
        self.direction = direction;

