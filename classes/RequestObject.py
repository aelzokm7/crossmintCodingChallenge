import json

class RequestObject:
    def __init__(self, url: str, body: dict = None, headers: dict = {}):
        self.url = url;
        self.body = json.dumps(body);
        self.headers = {"content-type": "application/json", **headers};

