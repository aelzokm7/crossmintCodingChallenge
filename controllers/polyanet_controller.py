import asyncio
import json;
import requests;
import time;
import os;
from dotenv import load_dotenv
from classes import RequestObject
from classes.Polyanet import Polyanet
from utils.map_utils import get_current_map_grid
from utils.request import make_request

load_dotenv()

# Variables
polyanets_endpoint = "https://challenge.crossmint.io/api/polyanets/"

# function to add polyanet to map
def add_polyanet_to_map(polyanet: Polyanet):
    request_object = RequestObject(polyanets_endpoint, "post", json.dumps({**polyanet.__dict__, "candidateId": os.getenv("CANDIDATE_ID")}));
    asyncio.run(make_request(request_object));

def delete_polyanet_from_map(polyanet: Polyanet):
    request_object = RequestObject(polyanets_endpoint, "delete", json.dumps({**polyanet.__dict__, "candidateId": os.getenv("CANDIDATE_ID")}));
    asyncio.run(make_request(request_object));

def delete_all_polyanets_from_map():
    grid = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] is not None:
                delete_polyanet_from_map(x,y);
    print("Successfully Deleted All Polyanets.")