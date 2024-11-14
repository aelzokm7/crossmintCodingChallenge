
class RequestObject:
    def __init__(self, url: str, method: str, body: dict, headers: dict):
        self.url = url;
        self.method = method;
        self.body = body;
        self.headers = {"content-type": "application/json"}.update(headers);

