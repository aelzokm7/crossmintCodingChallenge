import time
import aiohttp
import requests
from classes import RequestObject
from constants.constants import MAX_RETRY, RATE_LIMIT_TIME_DELAY;

async def make_request(request_object: RequestObject, method) -> dict:
    async with aiohttp.ClientSession() as session:
        try:
            print(f"Sending HTTP {method} Request.")
            response: aiohttp.ClientResponse = await session.request(method=method, url=request_object.url, data=request_object.body, headers=request_object.headers);
            if response.status == 429:
                retry: int = 0;
                while (response.status == 429 and retry < MAX_RETRY):
                    time.sleep(RATE_LIMIT_TIME_DELAY);
                    print("Rate Limit Reached. Retrying Request. Retry Count: ", (retry + 1));
                    # retry the request that triggered the rate limit in case it did not go through.
                    response: aiohttp.ClientResponse = await session.request(method=method, url=request_object.url, data=request_object.body, headers=request_object.headers);
                    retry += 1;
            elif not (response.ok):
                raise RuntimeError();
            response: dict = await response.json();   
        except requests.exceptions.RequestException as e:
            print("HTTP Request Failed. Please Try Again! Error: ", e);
            return {"failed": True}
        else:
            print("HTTP Request Was Successful!");
            return response;
