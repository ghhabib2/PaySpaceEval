import json
from enum import Enum
import requests
import aiohttp
import asyncio

class ContentType(Enum):
    """
    Different File statuses
    """
    Json = 100

async def send_secured_async_request(url, payload):
    """
    Sending an Async request to be processed
    :param url: URL
    :param payload: Payload
    :return: returned results
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            return await response.json()

def send_secured_request(url, payload, headers= None, content_type= None, sys_key = None):
    """
    Send a secured query based on the share key and return the result from the endpoint.

    :param str url : URL of the endpoint to send the request
    :param str payload: The content type json string to be sent with the request.
    :param str ContentType content_type: Content Type code
    :param str sys_key: System Key to connect a specific end-point
    :param dict headers: Headers for the data

    :return: (String of the content set by the system, Status Cod)
    :rtype: (dict, int)
    """

    if content_type == ContentType.Json:
        if headers is None and sys_key is not None:
            headers = {
                'syskey': sys_key, # TODO: Might need to change the way we are sending the system key
                'Content-Type': 'application/json'
            }
        elif headers is None:
            headers = {
                'Content-Type': 'application/json'
            }
        else:
            headers['Content-Type'] = 'application/json'
    # Send the request
    response = requests.request(method='POST', headers=headers, url= url, data=payload)

    return json.loads(response.content), response.status_code

def send_post_request(url, param: dict = None, data : dict = None , headers: dict = None, cookies : dict = None):
    """

    :param url:
    :param param:
    :param data:
    :param headers:
    :param cookies:
    :return:
    """

    print(url)

    response = requests.post(url)

    if response.status_code == 200 or response.status_code == 201:
        return response.content
    else:
        return None

def send_get_request(url, param: dict = None, data : dict = None , headers: dict = None, cookies : dict = None):
    """
    Send a Get request

    :param url:
    :param param:
    :param data:
    :param headers:
    :param cookies:
    :return:
    """

    response = requests.get(url)

    print(response)

    if response.status_code == 200:
        return response.content
    else:
        return None

def convert_to_dict(data):
    """
    Convert the content to readable data dictionary

    :param bytes data: data to be converted to dictionary

    :return: Data dictionary to be processed
    :rtype: dict
    """

    # Get the content of the HttpResponse as bytes
    content_bytes = data

    # Decode the content bytes into a string
    content_string = content_bytes.decode('utf-8')

    # Parse the content string into a dictionary using json.loads() for JSON content)
    content_dict = json.loads(content_string)

    return content_dict