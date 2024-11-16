from typing import List
from classes.Cometh import Cometh
from classes.Soloon import Soloon
from classes.SpaceObject import SpaceObject
from classes.Polyanet import Polyanet
from constants.constants import COMETH, POLYANET, SOLOON, SPACE_OBJECTS
import controllers.cometh_controller as cometh
import controllers.polyanet_controller as polyanet
import controllers.soloon_controller as soloon
from utils.map_utils import get_current_map_grid

def add_space_object_to_map(space_object: SpaceObject) -> None:
    """ Function to route a space object to proper add to map method. """

    if isinstance(space_object, Polyanet):
        polyanet.add_polyanet_to_map(space_object);
    elif isinstance(space_object, Cometh):
        cometh.add_cometh_to_map(space_object);
    elif isinstance(space_object, Soloon):
        soloon.add_soloon_to_map(space_object);
    else:
        print("Invalid Space Object!: ", space_object);

def delete_space_object_from_map(space_object: SpaceObject) -> None:
    """ Function to route a space object to proper delete from map method. """

    if isinstance(space_object, Polyanet):
        polyanet.delete_polyanet_from_map(space_object.row, space_object.column);
    elif isinstance(space_object, Cometh):
        cometh.delete_cometh_from_map(space_object.row, space_object.column);
    elif isinstance(space_object, Soloon):
        soloon.delete_soloon_from_map(space_object.row, space_object.column);
    else:
        print("Invalid Space Object!: ", space_object);

def delete_all_of_one_space_object_from_map(space_object: str) -> None:
    """ Function to route a space object to proper delete all from map method. """

    if (space_object == SPACE_OBJECTS["POLYANET"]):
        polyanet.delete_all_polyanets_from_map();
    elif (space_object == SPACE_OBJECTS["COMETH"]):
        cometh.delete_all_comeths_from_map();
    elif (space_object == SPACE_OBJECTS["SOLOON"]):
        soloon.delete_all_soloons_from_map();
    else:
        print("Invalid Space Object Type!: ", space_object);

def reset_map() -> None:
    """ Function to delete all space objects from map. """

    grid: List[List[dict]] = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    polyanet.delete_all_polyanets_from_map();
    cometh.delete_all_comeths_from_map();
    soloon.delete_all_soloons_from_map();
    remaining_objects: int = 0;
    grid = get_current_map_grid();
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if (grid[x][y] is not None):
                remaining_objects += 1;
    if (remaining_objects > 0):
        print(f"Failed To Delete {remaining_objects} Space Objects!");
    else:
        print("Map Has Been Cleared!");


