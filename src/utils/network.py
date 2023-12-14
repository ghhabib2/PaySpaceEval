import json
from enum import Enum
import requests

class ContentType(Enum):
    """
    Different File statuses
    """
    Json = 100

def send_secured_request(url, payload, content_type, sys_key):
    """
    Send a secured query based on the share key and return the result from the endpoint.

    :param str url : URL of the endpoint to send the request
    :param str payload: The content type json string to be sent with the request.
    :param ContentType content_type: Content Type code
    "param str sys_key: System Key to connect a specific end-point

    :return: (String of the content set by the system, Status Cod)
    :rtype: (dict, int)
    """
    headers = None
    if content_type == ContentType.Json:
        headers = {
            'syskey': sys_key,
            'Content-Type': 'application/json'
        }

    # Send the request
    response = requests.request(method='POST', headers=headers, url= url, data=payload)

    return convert_to_dict(response.content), response.status_code


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