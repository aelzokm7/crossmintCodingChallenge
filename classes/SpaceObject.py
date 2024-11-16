from abc import ABC

class SpaceObject(ABC):

    def __init__(self, row: int | str, column: int | str):
        self.row = row;
        self.column = column;