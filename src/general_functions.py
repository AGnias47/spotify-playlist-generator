#!/usr/bin/python3
#
#   A. Gnias
#   Created: 5/22/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Functions supporting use of the Spotify API
"""

from random import randint
import json
import requests
from src.Exceptions import UnsuccessfulGetRequest


def generate_random_string(length):
    text = str()
    for i in range(0, length):
        text += get_random_character()
    return text


def get_random_character():
    random_ascii_chars = [[65, 90], [97, 122], [48, 57]]
    rand_type = random_ascii_chars[randint(0, len(random_ascii_chars) - 1)]
    return chr(randint(rand_type[0], rand_type[1]))


def get_json_response_dict(oauth, search_url):
    """
    Returns a json dict from a REST GET request

    Parameters
    ----------
    oauth: str
        OAuth Token retrieved from Spotify
    search_url: str
        URL to query

    Returns
    -------
    dict
        Data returned from search_url GET request

    """
    headers = {"Content-Type": "application/json", "Authorization": "Bearer {0}".format(oauth)}
    try:
        response = requests.get(search_url, headers=headers)
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    if response.status_code != 200:
        raise UnsuccessfulGetRequest(f"Status Code: {response.status_code}")
    return json.loads(response.content.decode("utf-8"))


def print_pretty_json(json_data_loads):
    """
    Prints a formatted json to stdout

    Parameters
    ----------
    json_data_loads: dict
        json formatted as a dict by json library

    Returns
    -------
    None
        Prints to stdout

    """
    print(json.dumps(json_data_loads, indent=3, sort_keys=False))
    return None
