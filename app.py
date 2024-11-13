import json;
import requests;
import time;
import os;
from dotenv import load_dotenv

load_dotenv()

# API Endpoints
goal_endpoint = "https://challenge.crossmint.io/api/map/" + os.getenv("CANDIDATE_ID")
polyanets_endpoint = "https://challenge.crossmint.io/api/polyanets/"

# Phase 1 #
def phase1(size_of_cross):

# Get the map grid.
    response = requests.get(goal_endpoint);
    grid = response.json()["map"]["content"];

# Calculate the center of the grid.
# Since the grid is odd, this is straightforward as there is only one center.
# If the matrix was even, it would be more complicated since there isn't one center coordinate.
# However since the even case is not relevant to this challenge, I will skip it.

    center_width_of_grid = len(grid) // 2;
    center_height_of_grid = len(grid[0]) // 2;

# Search through the subgrid that will contain the cross.
# Check at each coordinate if it is diagonal to the center point using the below formula.
# If it is on a diagonal, call the api and populate that coordinate.

    for x in range(center_width_of_grid - size_of_cross, center_width_of_grid + size_of_cross + 1):
        for y in range(center_height_of_grid - size_of_cross, center_height_of_grid + size_of_cross + 1):
            if (abs(x - center_width_of_grid) == abs(y - center_height_of_grid)):
                response = requests.post(polyanets_endpoint, headers={"content-type": "application/json"}, data = json.dumps({"row": str(x), "column": str(y), "candidateId": os.getenv("CANDIDATE_ID")}));
                if response.status_code == 429:
                    time.sleep(5);
                    response = requests.post(polyanets_endpoint, headers={"content-type": "application/json"}, data = json.dumps({"row": str(x), "column": str(y), "candidateId": os.getenv("CANDIDATE_ID")}));

# Don't forget the main block

if __name__ == "__main__":

    # Input Parameters
    size_of_cross = 3;

    # function
    phase1(size_of_cross);



