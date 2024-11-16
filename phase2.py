from typing import List
from classes.Cometh import Cometh
from classes.Polyanet import Polyanet
from classes.Soloon import Soloon
from classes.SpaceObject import SpaceObject
from constants.constants import COMETH, POLYANET, SOLOON
from controllers.space_objects_controller import add_space_object_to_map, delete_all_of_one_space_object_from_map, delete_space_object_from_map
from utils.map_utils import get_goal_map_grid

# Phase 2 Script
def phase2() -> None:

    # Get the Goal Map.
    goal_grid = get_goal_map_grid();

    # Create a set to hold the space objects to be added to the current map grid.
    space_objects_set: set[SpaceObject] = set();

    # Loop through the goal map grid and create the appropriate space object.
    # Tokenize the values at each coordinate to determine the details of the space object to create.
    # After creating the space object, add it to the set.
    for x in range(0, len(goal_grid)):
        for y in range(0,len(goal_grid[0])):
            tokens: List[str] = goal_grid[x][y].split("_");
            object_name: str = tokens[-1].lower();
            if (object_name == POLYANET["name"]):
                space_objects_set.add(Polyanet(x, y));
            elif (object_name == COMETH["name"]):
                space_objects_set.add(Cometh(x, y, tokens[0]));
            elif (object_name == SOLOON["name"]):
                space_objects_set.add(Soloon(x, y, tokens[0]));
            else:
                pass;
    
    # Loop through the populated space object set and add each object to the current map grid.
    for space_object in space_objects_set:
        add_space_object_to_map(space_object); 

# Main Block
if __name__ == "__main__":

    cometh = Cometh(1, 1, "UP");
    print("COmeeth", type(cometh))
    print(cometh.__dict__)

    # phase2();