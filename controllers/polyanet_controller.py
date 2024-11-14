import json;
import requests;
import time;
import os;
from dotenv import load_dotenv

from utils.map_utils import get_map_grid

load_dotenv()

# Variables
polyanets_endpoint = "https://challenge.crossmint.io/api/polyanets/"
MAX_RETRY = 3;

# function to add polyanet to map
def add_polyanet_to_map(x, y):
    try:
        response = requests.post(polyanets_endpoint, headers={"content-type": "application/json"}, data = json.dumps({"row": str(x), "column": str(y), "candidateId": os.getenv("CANDIDATE_ID")}));
        # Timeout error
        if response.status_code == 429:
            retry = 0;
            while (response.status_code == 429 and retry < MAX_RETRY):
                time.sleep(5);
                # retry the request that triggered the rate limit in case it did not go through.
                response = requests.post(polyanets_endpoint, headers={"content-type": "application/json"}, data = json.dumps({"row": str(x), "column": str(y), "candidateId": os.getenv("CANDIDATE_ID")}));
                retry += 1;
        else: 
            response.raise_for_status();
    except requests.exceptions.RequestException as e:
        print("Failed to add polyanet. Error: ", e);
    print("Polyanet added successfully!")

def delete_polyanet_from_map(x, y):
    try:
        response = requests.post(polyanets_endpoint, headers={"content-type": "application/json"}, data = json.dumps({"row": str(x), "column": str(y), "candidateId": os.getenv("CANDIDATE_ID")}));
        response.raise_for_status();
    except requests.exceptions.RequestException as e:
        print("Failed to delete polyanet. Error: ", e);
    print("Polyanet Deleted Successfully!")


def delete_all_polyanet_from_map():
    grid = get_map_grid();
    if (grid is None or len(grid) == 0):
        print("Nothing to delete");
        return;
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            delete_polyanet_from_map(x,y);
    print("Successfully Deleted All Polyanets.")