import asyncio
import os
from typing import List
from dotenv import load_dotenv
from classes.RequestObject import RequestObject
from classes.Polyanet import Polyanet
from constants.constants import HTTP_DELETE, HTTP_POST, POLYANET, POLYANETS_ENDPOINT
from utils.map_utils import get_current_map_grid
from utils.request import make_request

load_dotenv()

def add_polyanet_to_map(polyanet: Polyanet) -> None:
    """ Function to add a polyanet to the map. """
        
    print("Adding Polyanet To Map.");
    request_object: RequestObject = RequestObject(POLYANETS_ENDPOINT, {**polyanet.__dict__, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_POST));
    if (response.get("failed")):
        print(f"Unable To Add Cometh At ({polyanet.row}, {polyanet.column}) To Map.");
        return;
    print(f"Successfully Added Cometh To Map At ({polyanet.row}, {polyanet.column})!");

def delete_polyanet_from_map(row: int, column: int) -> None:
    """ Function to delete a polyanet from the map. """

    print("Deleting Polyanet From Map.");
    request_object: RequestObject = RequestObject(POLYANETS_ENDPOINT, {"row": row, "column": column, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_DELETE));
    if (response.get("failed")):
        print(f"Unable To Delete Polyanet At ({row}, {column}) From Map.");
        return;
    print(f"Successfully Deleted Polyanet At ({row}, {column}) From Map!");

def delete_all_polyanets_from_map() -> None:
    """ Function to delete all polyanets from the map. """

    grid: List[List[dict]] = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if (grid[x][y] is not None and grid[x][y].get("type") == POLYANET["type"]):
                delete_polyanet_from_map(x,y);