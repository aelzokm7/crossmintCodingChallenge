from classes.SpaceObject import SpaceObject
from constants.constants import SOLOON_COLORS

class Soloon(SpaceObject):

    def __new__(cls, row: int | str, column: int | str, color: int | str):
        color = color.lower();
        try: 
            if not (color in SOLOON_COLORS):
                raise ValueError("Color Has To Be One Of The Following: " + str(SOLOON_COLORS));
        except ValueError as e:
            print(e);
        else:
            return super().__new__(cls);

    def __init__(self, row: int | str, column: int | str, color: str):
        color = color.lower();
        super().__init__(row, column);
        self.color = color;
        

