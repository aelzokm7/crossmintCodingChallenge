import asyncio
import os
from typing import List
from classes.Soloon import Soloon
from classes.RequestObject import RequestObject
from constants.constants import HTTP_DELETE, HTTP_POST, SOLOON, SOLOONS_ENDPOINT
from utils.map_utils import get_current_map_grid
from utils.request import make_request
from dotenv import load_dotenv

load_dotenv()

def add_soloon_to_map(soloon: Soloon) -> None:
    """ Function to add a soloon to the map. """

    print("Adding Soloon To Map.");
    request_object: RequestObject = RequestObject(SOLOONS_ENDPOINT, {**soloon.__dict__, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_POST));
    if (response.get("failed")):
        print(f"Unable To Add Soloon At ({soloon.row}, {soloon.column}) To Map.");
        return;
    print(f"Successfully Added Soloon To Map At ({soloon.row}, {soloon.column})!");

def delete_soloon_from_map(row: int, column: int) -> None:
    """ Function to delete a soloon from the map. """

    print("Deleting Soloon From Map.");
    request_object: RequestObject = RequestObject(SOLOONS_ENDPOINT, {"row": row, "column": column, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_DELETE));
    if (response.get("failed")):
        print(f"Unable To Delete Soloon At ({row}, {column}) From Map.");
        return;
    print(f"Successfully Deleted Soloon At ({row}, {column}) From Map!");

def delete_all_soloons_from_map() -> None:
    """ Function to delete all soloons from the map. """

    grid: List[List[dict]] = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if (grid[x][y] is not None and grid[x][y].get("type") == SOLOON["type"]):
                delete_soloon_from_map(x, y);

