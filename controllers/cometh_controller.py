

# variables
from classes import Cometh, RequestObject
from utils.map_utils import get_current_map_grid
from utils.request import make_request


comeths_endpoint = "https://challenge.crossmint.io/api/comeths/"


# function to add cometh to map

def add_cometh_to_map(cometh: Cometh):
    request_object = RequestObject(comeths_endpoint, "post", cometh.__dict__);
    make_request(request_object);

# function to delete cometh from map
def delete_cometh_from_map(cometh: Cometh):
    request_object = RequestObject(comeths_endpoint, "delete", cometh.__dict__);
    make_request(request_object);

# function to delete all comeths from map
def delete_all_comeths_from_map():
    grid = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] is not None:
                delete_cometh_from_map(x,y);
    print("Successfully Deleted All Polyanets.")

