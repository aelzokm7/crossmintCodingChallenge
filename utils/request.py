import time
import aiohttp
import requests
from classes import RequestObject;

# variables
MAX_RETRY = 3;

async def make_request(request_object: RequestObject):
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        try:
            response = await session.request(method=request_object.method, url=request_object.url, data=request_object.body, headers=request_object.headers);
            await response.json();
            if response.status == 429:
                retry = 0;
                while (response.status == 429 and retry < MAX_RETRY):
                    time.sleep(5);
                    # retry the request that triggered the rate limit in case it did not go through.
                    response = await session.request(method=request_object.method, url=request_object.url, data=request_object.body, headers=request_object.headers);
                    retry += 1;
        except requests.exceptions.RequestException as e:
            print(f"Failed To WORD BASED ON CALL HERE {type(request_object).__name__}. Error: ", e);
        print(f"{type(request_object).__name__} WORD BASED ON CALL HERE Successfully!")
