import classes;
import classes.Soloon
import controllers.cometh_controller as cometh
import controllers.polyanet_controller as polyanet
import controllers.soloon_controller as soloon
from utils.map_utils import get_current_map_grid;
from utils.request import make_request;


# function to add a space object to map
def add_space_object_to_map(space_object: classes.SpaceObject):
    match isinstance(space_object):
        case classes.Polyanet:
            polyanet.add_polyanet_to_map(space_object);
        case classes.Cometh:
            cometh.add_cometh_to_map(space_object);
        case classes.Soloon:
            soloon.add_soloon_to_map(space_object);
        case _:
            print("Invalid Space Object");

# function to delete a space object from map
def delete_space_object_from_map(space_object: classes.SpaceObject):
    match isinstance(space_object):
        case classes.Polyanet:
            polyanet.delete_polyanet_from_map(space_object);
        case classes.Cometh:
            cometh.delete_cometh_from_map(space_object);
        case classes.Soloon:
            soloon.delete_soloon_from_map(space_object);
        case _:
            print("Invalid Space Object");

def delete_all_of_one_space_object_from_map(space_object: classes.SpaceObject):
        match isinstance(space_object):
            case classes.Polyanet:
                polyanet.delete_all_polyanets_from_map();
            case classes.Cometh:
                cometh.delete_all_comeths_from_map();
            case classes.Soloon:
                soloon.delete_all_soloons_from_map();
            case _:
                print("Invalid Space Object");

# function to reset map
def reset_map():
    grid = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] is not None:
                polyanet.delete_all_polyanets_from_map();
                cometh.delete_all_comeths_from_map();
                soloon.delete_all_soloons_from_map();
    print("Successfully Deleted All Objects.")


