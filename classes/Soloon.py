from classes.SpaceObject import SpaceObject
from constants import SOLOONS_COLORS

class Soloon(SpaceObject):

    def __init__(self, row: int, column: int, color: str):
        super().__init__(row, column)

        if not (color.lower() in SOLOONS_COLORS):
            raise ValueError("Color has to be one of the following: " + str(SOLOONS_COLORS));
        
        self.color = color;
        

