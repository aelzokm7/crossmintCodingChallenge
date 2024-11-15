import asyncio
import os
from typing import List;
from dotenv import load_dotenv
from classes.RequestObject import RequestObject
from constants import CURRENT, CURRENT_MAP_ENDPOINT, GOAL, GOAL_MAP_ENDPOINT, HTTP_GET
from utils.request import make_request
import controllers.cometh_controller as cometh
import controllers.polyanet_controller as polyanet
import controllers.soloon_controller as soloon

load_dotenv()

# Get the map grid.
def get_map_grid(map: str) -> List[List[str]]:
    grid = None;
    try:
        if (map.lower() == GOAL):
            request_object: RequestObject = RequestObject(GOAL_MAP_ENDPOINT.format(os.getenv("CANDIDATE_ID")));
            response: dict = asyncio.run(make_request(request_object, HTTP_GET));
            grid = response["goal"];
        elif (map.lower() == CURRENT):
            request_object: RequestObject = RequestObject(CURRENT_MAP_ENDPOINT + os.getenv("CANDIDATE_ID"));
            response: dict = asyncio.run(make_request(request_object, HTTP_GET));
            grid = response["map"]["content"];
        else:
            print("Invalid Map Request. Either 'goal' or 'current'.")
    except:
        print("Failed to retrieve map.");
    else:
        return grid;

# function to reset map
def reset_map() -> None:
    grid = get_map_grid("current");
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    polyanet.delete_all_polyanets_from_map();
    cometh.delete_all_comeths_from_map();
    soloon.delete_all_soloons_from_map();
    print("Successfully Deleted All Objects.")

