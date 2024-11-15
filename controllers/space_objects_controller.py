from typing import List
from classes.Cometh import Cometh
from classes.Soloon import Soloon
from classes.SpaceObject import SpaceObject
from classes.Polyanet import Polyanet
from constants.constants import COMETH, POLYANET, SOLOON
import controllers.cometh_controller as cometh
import controllers.polyanet_controller as polyanet
import controllers.soloon_controller as soloon


# function to add a space object to map
def add_space_object_to_map(space_object: SpaceObject) -> None:
    if isinstance(space_object, Polyanet):
        polyanet.add_polyanet_to_map(space_object);
    elif isinstance(space_object, Cometh):
        cometh.add_cometh_to_map(space_object);
    elif isinstance(space_object, Soloon):
        soloon.add_soloon_to_map(space_object);
    else:
        print("Invalid Space Object!: ", space_object);

# function to delete a space object from map
def delete_space_object_from_map(space_object: SpaceObject) -> None:
    if isinstance(space_object, Polyanet):
        polyanet.delete_polyanet_from_map(space_object.row, space_object.column);
    elif isinstance(space_object, Cometh):
        cometh.delete_cometh_from_map(space_object.row, space_object.column);
    elif isinstance(space_object, Soloon):
        soloon.delete_soloon_from_map(space_object.row, space_object.column);
    else:
        print("Invalid Space Object!: ", space_object);

def delete_all_of_one_space_object_from_map(space_object_type: int) -> None:
    if (space_object_type == POLYANET["type"]):
        polyanet.delete_all_polyanets_from_map();
    elif (space_object_type == COMETH["type"]):
        cometh.delete_all_comeths_from_map();
    elif (space_object_type == SOLOON["type"]):
        soloon.delete_all_soloons_from_map();
    else:
        print("Invalid Space Object Type!: ", space_object_type);


