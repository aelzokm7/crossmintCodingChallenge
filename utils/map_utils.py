import asyncio
import os
from typing import List;
from dotenv import load_dotenv
from classes.RequestObject import RequestObject
from constants import CURRENT_MAP_ENDPOINT, GOAL_MAP_ENDPOINT, HTTP_GET
from utils.request import make_request

load_dotenv()

# Get the map grid.
def get_map_grid(map: str) -> List[List[str]]:
    grid = None;
    try:
        if (map.lower() == "goal"):
            request_object = RequestObject(GOAL_MAP_ENDPOINT.format(os.getenv("CANDIDATE_ID")));
            response = asyncio.run(make_request(request_object, HTTP_GET));
            grid = grid = response["goal"];
        elif (map.lower() == "current"):
            request_object = RequestObject(CURRENT_MAP_ENDPOINT + os.getenv("CANDIDATE_ID"));
            response = asyncio.run(make_request(request_object, HTTP_GET));
            grid = response["map"]["content"];
        else:
            print("Invalid Map Request. Either 'goal' or 'current'.")
    except:
        print("Failed to retrieve map.");
    else:
        return grid;


