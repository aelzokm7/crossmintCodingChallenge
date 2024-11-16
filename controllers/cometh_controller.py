import asyncio
import os
from typing import List
from classes.Cometh import Cometh
from classes.RequestObject import RequestObject
from constants.constants import COMETH, COMETHS_ENDPOINT, HTTP_DELETE, HTTP_POST
from utils.map_utils import get_current_map_grid
from utils.request import make_request
from dotenv import load_dotenv

load_dotenv()

def add_cometh_to_map(cometh: Cometh) -> None:
    """ Function to add a cometh to the map. """

    print("Adding Cometh To Map.");
    request_object: RequestObject = RequestObject(COMETHS_ENDPOINT, {**cometh.__dict__, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_POST));
    if (response.get("failed")):
        print(f"Unable To Add Cometh At ({cometh.row}, {cometh.column}) To Map.");
        return;
    print(f"Successfully Added Cometh To Map At ({cometh.row}, {cometh.column})!");

def delete_cometh_from_map(row: int, column: int) -> None:
    """ Function to delete a cometh from the map. """

    print("Deleting Cometh From Map.");
    request_object: RequestObject = RequestObject(COMETHS_ENDPOINT, {"row": row, "column": column, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_DELETE));
    if (response.get("failed")):
        print(f"Unable To Delete Cometh At ({row}, {column}) From Map.");
        return;
    print(f"Successfully Deleted Cometh At ({row}, {column}) From Map!");

def delete_all_comeths_from_map() -> None:
    """ Function to delete all comeths from the map. """

    grid: List[List[dict]] = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if (grid[x][y] is not None and (grid[x][y]).get("type") == COMETH["type"]):
                delete_cometh_from_map(x,y);
