import asyncio
import json
import os
from classes.Soloon import Soloon
from classes.RequestObject import RequestObject
from utils.map_utils import get_current_map_grid
from utils.request import make_request
from dotenv import load_dotenv

load_dotenv()

# variables
soloons_endpoint = "https://challenge.crossmint.io/api/soloons/"


# function to add soloon to map

def add_soloon_to_map(soloon: Soloon):
    request_object = RequestObject(soloons_endpoint, "post", json.dumps({**soloon.__dict__, "candidateId": os.getenv("CANDIDATE_ID")}));
    asyncio.run(make_request(request_object));

# function to delete soloon from map
def delete_soloon_from_map(soloon: Soloon):
    request_object = RequestObject(soloons_endpoint, "delete", json.dumps({**soloon.__dict__, "candidateId": os.getenv("CANDIDATE_ID")}));
    asyncio.run(make_request(request_object));

# function to delete all soloon from map
def delete_all_soloons_from_map():
    grid = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing To Delete.");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if grid[x][y] is not None:
                delete_soloon_from_map(x,y);
    print("Successfully Deleted.")

