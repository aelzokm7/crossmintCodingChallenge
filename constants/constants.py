# General Variables
MAX_RETRY = 3;
RATE_LIMIT_TIME_DELAY = 10;

# Endpoints
GOAL_MAP_ENDPOINT = "https://challenge.crossmint.io/api/map/{}/goal";
CURRENT_MAP_ENDPOINT = "https://challenge.crossmint.io/api/map/";
POLYANETS_ENDPOINT = "https://challenge.crossmint.io/api/polyanets/";
COMETHS_ENDPOINT = "https://challenge.crossmint.io/api/comeths/";
SOLOONS_ENDPOINT = "https://challenge.crossmint.io/api/soloons/";
API_ENDPOINT = "https://challenge.crossmint.io/api/{}/";

# Space Objects Values and Constraints
COMETHS_DIRECTIONS = {"up", "down", "left", "right"};
SOLOONS_COLORS = {"red", "blue", "purple", "white"};
SPACE_OBJECTS = {"polyanets": {"name": "polyanets", "type": 0}, 
                 "comeths": {"name": "comeths", "type": 2},
                 "soloons": {"name": "soloons", "type": 1}};

# HTTP_METHODS
HTTP_POST = "POST";
HTTP_GET = "GET";
HTTP_DELETE = "DELETE";

# String Literals
POLYANET = "POLYANET";
COMETH = "COMETH";
SOLOON = "SOLOON";

