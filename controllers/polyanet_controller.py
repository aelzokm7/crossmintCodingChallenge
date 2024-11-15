import asyncio
import os;
from dotenv import load_dotenv
from classes.RequestObject import RequestObject
from classes.Polyanet import Polyanet
from constants import HTTP_DELETE, HTTP_POST, POLYANET, POLYANETS_ENDPOINT
from utils.map_utils import get_map_grid
from utils.request import make_request

load_dotenv()

# function to add polyanet to map
def add_polyanet_to_map(polyanet: Polyanet) -> None:
    request_object = RequestObject(POLYANETS_ENDPOINT, {**polyanet.__dict__, "candidateId": os.getenv("CANDIDATE_ID")});
    asyncio.run(make_request(request_object, HTTP_POST));

def delete_polyanet_from_map(row: int, column: int) -> None:
    request_object = RequestObject(POLYANETS_ENDPOINT, {"row": row, "column": column, "candidateId": os.getenv("CANDIDATE_ID")});
    asyncio.run(make_request(request_object, HTTP_DELETE));

def delete_all_polyanets_from_map() -> None:
    grid = get_map_grid("current");
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] is not None and grid[x][y]["type"] == POLYANET["type"]:
                delete_polyanet_from_map(x,y);
    print("Successfully Deleted All Polyanets.")