import requests;
import os;
from dotenv import load_dotenv

load_dotenv()

# Variables
current_map_endpoint = "https://challenge.crossmint.io/api/map/" + os.getenv("CANDIDATE_ID");
goal_map_endpoint = "https://challenge.crossmint.io/api/map/" + os.getenv("CANDIDATE_ID") + "/goal";

# Get the goal map grid.
def get_goal_map_grid():
    grid = None;
    try:
        response = requests.get(goal_map_endpoint);
        response.raise_for_status();
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve map. Error: ", e);
    else:
        grid = response.json()["goal"];
        return grid;

# Get the current map grid.
def get_current_map_grid():
    grid = None;
    try:
        response = requests.get(current_map_endpoint);
        response.raise_for_status();
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve map. Error: ", e);
    else:
        grid = response.json()["map"]["content"];
        return grid;


