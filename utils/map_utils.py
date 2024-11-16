import asyncio
import os
from typing import List
from dotenv import load_dotenv
from classes.RequestObject import RequestObject
from constants.constants import CURRENT_MAP_ENDPOINT, GOAL_MAP_ENDPOINT, HTTP_GET
from utils.request import make_request

load_dotenv()

def get_goal_map_grid() -> List[List[str]]:
    """ Function to retrieve goal map. 
        :returns: A 2D matrix of strings.
    """

    grid: List[List[str]] = None;
    print("Retrieving Goal Map.");
    request_object: RequestObject = RequestObject(GOAL_MAP_ENDPOINT.format(os.getenv("CANDIDATE_ID")));
    response: dict = asyncio.run(make_request(request_object, HTTP_GET));
    if (response.get("failed")):
        print("Failed To Retrieve Map.");
        return grid;
    grid = response.get("goal");
    return grid;

def get_current_map_grid() -> List[List[dict]]:
    """ Function to retrieve current map. 
        :returns: A 2D matrix of objects.
    """

    grid: List[List[dict]] = None;
    print("Retrieving Current Map.");
    request_object: RequestObject = RequestObject(CURRENT_MAP_ENDPOINT + os.getenv("CANDIDATE_ID"));
    response: dict = asyncio.run(make_request(request_object, HTTP_GET));
    if (response.get("failed")):
        print("Failed To Retrieve Map.");
        return grid;
    if (response.get("map")):
        grid = (response.get("map")).get("content");
    return grid;

