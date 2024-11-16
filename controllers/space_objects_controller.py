import asyncio
import os
from typing import List
from dotenv import load_dotenv
from classes.RequestObject import RequestObject
from classes.SpaceObject import SpaceObject
from constants.constants import API_ENDPOINT, HTTP_DELETE, HTTP_POST, SPACE_OBJECTS
from utils.map_utils import get_current_map_grid
from utils.request import make_request

load_dotenv();

def add_space_object_to_map(space_object: SpaceObject) -> None:
    """ Function to add a space object to the map. """

    if not (issubclass(type(space_object), SpaceObject)):
        print("Invalid Space Object!: ", space_object);
        return;
    name: str = space_object.__class__.__name__.lower();
    print(f"Adding a {name} To Map.");
    request_object: RequestObject = RequestObject(API_ENDPOINT.format(name), {**space_object.__dict__, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_POST));
    if (response.get("failed")):
        print(f"Unable To Add {name} At ({space_object.row}, {space_object.column}) To Map.");
        return;
    print(f"Successfully Added {name} To Map At ({space_object.row}, {space_object.column})!");

def delete_space_object_from_map(space_object: SpaceObject) -> None:
    """ Function to parse a space object before delete from map method. """

    if not (issubclass(type(space_object), SpaceObject)):
        print("Invalid Space Object!: ", space_object);
        return;
    name: str = space_object.__class__.__name__.lower();
    delete_from_map(name, space_object.row, space_object.column);

def delete_all_of_one_space_object_type_from_map(name: str) -> None:
    """ Function to delete all space objects of a single type from the map. """

    name = name.lower();
    if not (SPACE_OBJECTS.get(name)):
        print("Invalid Space Object Name!");
        return;
    object_type: int = SPACE_OBJECTS.get(name).get("type");
    grid: List[List[dict]] = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("No Grid Exists.");
        return;
    print(f"Starting Deletion Of All {name} From Map.");
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if (grid[x][y] is not None and grid[x][y].get("type") == object_type):
                delete_from_map(name, x,y);

def delete_from_map(name: str, row: int, column: int) -> None:
    """ Function to delete a space object from the map. """

    print(f"Deleting a {name} From Map.");
    request_object: RequestObject = RequestObject(API_ENDPOINT.format(name), {"row": row, "column": column, "candidateId": os.getenv("CANDIDATE_ID")});
    response: dict = asyncio.run(make_request(request_object, HTTP_DELETE));
    if (response.get("failed")):
        print(f"Unable To Delete {name} At ({row}, {column}) From Map.");
        return;
    print(f"Successfully Deleted {name} At ({row}, {column}) From Map!");

def reset_map() -> None:
    """ Function to delete all space objects from map. """

    grid: List[List[dict]] = get_current_map_grid();
    if (grid is None or len(grid) == 0):
        print("No Grid Exists.");
        return;
    for key in SPACE_OBJECTS.keys():
        delete_all_of_one_space_object_type_from_map(SPACE_OBJECTS[key].get("name"));
    remaining_objects: int = 0;
    grid = get_current_map_grid();
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            if (grid[x][y] is not None):
                remaining_objects += 1;
    if (remaining_objects > 0):
        print(f"Failed To Delete {remaining_objects} Space Objects!");
    else:
        print("Map Has Been Cleared!");