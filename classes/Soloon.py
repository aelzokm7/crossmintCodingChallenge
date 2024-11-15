from classes.SpaceObject import SpaceObject
from constants.constants import SOLOON_COLORS

class Soloon(SpaceObject):

    def __init__(self, row: int | str, column: int | str, color: str):
        super().__init__(row, column)

        color = color.lower();

        if not (color in SOLOON_COLORS):
            raise ValueError("Color Has To Be One Of The Following: " + str(SOLOON_COLORS));
        
        self.color = color;
        

