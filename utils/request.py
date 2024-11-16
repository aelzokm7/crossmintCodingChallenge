import time
import aiohttp
from classes import RequestObject
from constants.constants import MAX_RETRY, RATE_LIMIT_TIME_DELAY

async def make_request(request_object: RequestObject, method: str) -> dict:
    """ Function to make an HTTP request. 
        :param request_object: An object of class RequestObject that contains the url, body, and headers of HTTP request.   
        :param method: A string literal of a valid HTTP method type.
        :return: A JSON form of the response object on success or a dict with a failed attribute set to True on failure.
    """

    async with aiohttp.ClientSession() as session:
        final_response: dict = {};
        try:
            print(f"Sending HTTP {method} Request.");
            response: aiohttp.ClientResponse = await session.request(method=method, url=request_object.url, data=request_object.body, headers=request_object.headers);
            response.raise_for_status();
            final_response = await response.json();
        except aiohttp.ClientResponseError as e:
            if (e.status == 429):
                retry: int = 0;
                while (e.status == 429 and retry < MAX_RETRY):
                    time.sleep(RATE_LIMIT_TIME_DELAY);
                    retry += 1;
                    print("Rate Limit Reached. Retrying Request. Retry Count: ", retry);
                    response: aiohttp.ClientResponse = await session.request(method=method, url=request_object.url, data=request_object.body, headers=request_object.headers);
                    e.status = response.status
            elif not (e.status < 400):
                print("HTTP Request Failed. Please Try Again! Error: ", e);
                final_response.set("failed", True);
        except aiohttp.ClientError as e:   
            print("An error occured!: ", e);
            final_response.set("failed", True);
        else:
            print("HTTP Request Was Successful!");
        finally:
            return final_response;
