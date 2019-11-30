#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   general_functions.py - Functions supporting use of the Spotify API
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0


import json
import requests


def get_json_response_dict(oauth, search_url):
    """
    Returns a json dict from a REST get request
    Input: OAuth token and Search URL
    Return Value: Json returned from request as a dict
    """
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(oauth)}
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        print("catch errors here")
        return "Something bad here"
    return json.loads(response.content.decode("utf-8"))


def print_pretty_json(json_data_loads):
    """
    Prints a formatted json to stdout
    Input: json formatted as a dict by Python JSON library
    Return Value: None (prints to stdout)
    """
    print(json.dumps(json_data_loads, indent=3, sort_keys=False))
