from classes.SpaceObject import SpaceObject

class Soloon(SpaceObject):
    
    colors = ["red", "blue", "purple", "white"];

    def __init__(self, row, column, color):
        super().__init__(row, column)
        self.direction = color;
        

