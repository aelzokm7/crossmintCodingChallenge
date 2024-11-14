import requests;
import os;
from dotenv import load_dotenv

load_dotenv()

# Variables
goal_endpoint = "https://challenge.crossmint.io/api/map/" + os.getenv("CANDIDATE_ID")

# Get the map grid.
def get_map_grid():
    grid = None;
    try:
        response = requests.get(goal_endpoint);
        response.raise_for_status();
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve map. Error: ", e);
    else:
        grid = response.json()["map"]["content"];
        return grid;

