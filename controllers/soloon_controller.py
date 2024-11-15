import asyncio
import os
from classes.Soloon import Soloon
from classes.RequestObject import RequestObject
from constants import HTTP_DELETE, HTTP_POST, SOLOON, SOLOONS_ENDPOINT
from utils.map_utils import get_map_grid
from utils.request import make_request
from dotenv import load_dotenv

load_dotenv()

# function to add soloon to map

def add_soloon_to_map(soloon: Soloon) -> None:
    request_object: RequestObject = RequestObject(SOLOONS_ENDPOINT, {**soloon.__dict__, "candidateId": os.getenv("CANDIDATE_ID")});
    asyncio.run(make_request(request_object, HTTP_POST));

# function to delete soloon from map
def delete_soloon_from_map(row: int, column: int) -> None:
    request_object: RequestObject = RequestObject(SOLOONS_ENDPOINT, {"row": row, "column": column, "candidateId": os.getenv("CANDIDATE_ID")});
    asyncio.run(make_request(request_object, HTTP_DELETE));

# function to delete all soloon from map
def delete_all_soloons_from_map() -> None:
    grid = get_map_grid("current");
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] is not None and grid[x][y]["type"] == SOLOON["type"]:
                delete_soloon_from_map(x, y);
    print("Successfully Deleted.")

