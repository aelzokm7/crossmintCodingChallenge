from classes.SpaceObject import SpaceObject
from constants.constants import COMETHS_DIRECTIONS

class Comeths(SpaceObject):

    def __new__(cls, row: int | str, column: int | str, direction: int | str):
        direction = direction.lower();
        try: 
            if not (direction in COMETHS_DIRECTIONS):
                raise ValueError("Direction Has To Be One Of The Following: " + str(COMETHS_DIRECTIONS));
        except ValueError as e:
            print(e);
        else:
            return super().__new__(cls);

    def __init__(self, row: int | str, column: int | str, direction: str):
        direction = direction.lower();
        super().__init__(row, column);
        self.direction = direction;

