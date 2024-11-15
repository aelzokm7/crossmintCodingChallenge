import asyncio
import os
from classes.Cometh import Cometh
from classes.RequestObject import RequestObject
from constants import COMETH, COMETHS_ENDPOINT, HTTP_DELETE, HTTP_POST
from utils.map_utils import get_map_grid
from utils.request import make_request
from dotenv import load_dotenv

load_dotenv()

# function to add cometh to map

def add_cometh_to_map(cometh: Cometh) -> None:
    request_object: RequestObject = RequestObject(COMETHS_ENDPOINT, {**cometh.__dict__, "candidateId": os.getenv("CANDIDATE_ID")});
    asyncio.run(make_request(request_object, HTTP_POST));

# function to delete cometh from map
def delete_cometh_from_map(row: int, column: int) -> None:
    request_object: RequestObject = RequestObject(COMETHS_ENDPOINT, {"row": row, "column": column, "candidateId": os.getenv("CANDIDATE_ID")});
    asyncio.run(make_request(request_object, HTTP_DELETE));

# function to delete all comeths from map
def delete_all_comeths_from_map() -> None:
    grid = get_map_grid("current");
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] is not None and grid[x][y]["type"] == COMETH["type"]:
                delete_cometh_from_map(x,y);
    print("Successfully Deleted.")

