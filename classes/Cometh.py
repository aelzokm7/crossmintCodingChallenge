from classes.SpaceObject import SpaceObject
from constants.constants import COMETH_DIRECTIONS

class Cometh(SpaceObject):

    def __new__(cls, row: int | str, column: int | str, direction: int | str):
        direction = direction.lower();
        try: 
            if not (direction in COMETH_DIRECTIONS):
                raise ValueError("Direction Has To Be One Of The Following: " + str(COMETH_DIRECTIONS));
        except ValueError as e:
            print(e);
        else:
            return super().__new__(cls);

    def __init__(self, row: int | str, column: int | str, direction: str):
        direction = direction.lower();
        super().__init__(row, column);
        self.direction = direction;

