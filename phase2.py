from typing import List
from classes.Cometh import Cometh
from classes.Polyanet import Polyanet
from classes.Soloon import Soloon
from classes.SpaceObject import SpaceObject
from constants import COMETH, CURRENT, GOAL, POLYANET, SOLOON
from controllers.space_objects_controller import add_space_object_to_map, delete_all_of_one_space_object_from_map, delete_space_object_from_map, reset_map
from utils.map_utils import get_map_grid

def phase2() -> None:

    # Get the Goal Map
    goal_grid = get_map_grid(GOAL);
    print(goal_grid);
    space_objects_set: set[SpaceObject] = set();

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
    
    for space_object in space_objects_set:
        add_space_object_to_map(space_object); 
    
    final_map = get_map_grid(CURRENT);
    
    print(final_map);
    
    return None;



if __name__ == "__main__":

    phase2();