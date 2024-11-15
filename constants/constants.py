# General Variables
MAX_RETRY = 3;
RATE_LIMIT_TIME_DELAY = 5;

# Endpoints
GOAL_MAP_ENDPOINT = "https://challenge.crossmint.io/api/map/{}/goal";
CURRENT_MAP_ENDPOINT = "https://challenge.crossmint.io/api/map/";
POLYANETS_ENDPOINT = "https://challenge.crossmint.io/api/polyanets/";
COMETHS_ENDPOINT = "https://challenge.crossmint.io/api/comeths/";
SOLOONS_ENDPOINT = "https://challenge.crossmint.io/api/soloons/";

# Space Objects Values and Constraints
SPACE_OBJECTS = {"POLYANET": "polyanet", "COMETH": "cometh", "SOLOON": "soloon"}
COMETH_DIRECTIONS = {"up", "down", "left", "right"};
SOLOON_COLORS = {"red", "blue", "purple", "white"};
POLYANET = {"name": "polyanet", "type": 0}
COMETH = {"name": "cometh", "type": 2}
SOLOON = {"name": "soloon", "type": 1}

# HTTP_METHODS
HTTP_POST = "POST";
HTTP_GET = "GET";
HTTP_DELETE = "DELETE";