import asyncio
import os
from typing import List;
from dotenv import load_dotenv
from classes.RequestObject import RequestObject
from constants.constants import CURRENT_MAP_ENDPOINT, GOAL_MAP_ENDPOINT, HTTP_GET
from utils.request import make_request
import controllers.cometh_controller as cometh
import controllers.polyanet_controller as polyanet
import controllers.soloon_controller as soloon

load_dotenv()

# Get the goal map grid.
def get_goal_map_grid() -> List[List[str]]:
    grid: List[List[str]] = None;
    try:
            print("Retrieving Goal Map.");
            request_object: RequestObject = RequestObject(GOAL_MAP_ENDPOINT.format(os.getenv("CANDIDATE_ID")));
            response: dict = asyncio.run(make_request(request_object, HTTP_GET));
            grid: List[List[str]] = response.get("goal");
    except:
        print("Failed to retrieve map.");
    else:
        return grid;

# Get the current map grid.
def get_current_map_grid() -> List[List[dict]]:
    grid: List[List[dict]] = None;
    try:
            print("Retrieving Current Map.");
            request_object: RequestObject = RequestObject(CURRENT_MAP_ENDPOINT + os.getenv("CANDIDATE_ID"));
            response: dict = asyncio.run(make_request(request_object, HTTP_GET));
            grid: List[List[dict]] = response.get("map").get("content");
    except:
        print("Failed to retrieve map.");
    else:
        return grid;

# function to reset map
def reset_map() -> None:
    grid: List[List[dict]] = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    polyanet.delete_all_polyanets_from_map();
    cometh.delete_all_comeths_from_map();
    soloon.delete_all_soloons_from_map();
    print("Map Has Been Cleared!");

