#!/usr/bin/env python3
#
#   A. Gnias
#   Created: 5/20/2020
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Functions interacting with keys JSON file. Keys file format should be:

.. code-block:: json

    {
        "client_id": "<Your Client ID>",
        "client_secret": "<Your Client Secret ID>",
        "access_token": "<Access Token>",
        "refresh_token": "<Refresh Token>"
    }
"""

import argparse
from base64 import b64encode
import json
import requests


def refresh_spotify_access_token(keys_filename="keys.json", output_file=None):
    """
    Refreshes the access token in a json file with the contents:

    .. code-block:: json

        {
            "client_id": "client id",
            "client_secret": "client secret",
            "access_token": "access token",
            "refresh_token": "refresh token"
        }

    Parameters
    ----------
    keys_filename: str (default is "keys.json")
        Path to json file
    output_file: str (default is None)
        Path to save updated json file; if None, update the file that was loaded

    Returns
    -------
    None
        Value for access_token is modified for the file in place or in output_file

    """
    with open(keys_filename) as K:
        keys = json.load(K)

    # Get values from json
    client_id = keys["client_id"]
    client_secret = keys["client_secret"]
    refresh_token = keys["refresh_token"]

    # Encode client_id:client_secret
    encoding = b64encode(f"{client_id}:{client_secret}".encode("UTF-8")).decode("UTF-8")

    # Define headers and data payload
    headers = {"Authorization": f"Basic {encoding}"}
    data = {"grant_type": "refresh_token", "refresh_token": f"{refresh_token}"}

    # Send post command
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    # Get the new access token from the response and set it within the keys dict
    new_access_token = json.loads(response.content)["access_token"]
    keys["access_token"] = new_access_token

    # Save the new access token to the same file, or a new file if output_file is specified. Other values are unchanged
    if output_file:
        keys_filename = output_file
    with open(keys_filename, "w") as K:
        json.dump(keys, K, indent=4)
    return None


def get_access_token(keys_filename="keys.json"):
    """
    Gets the access_token value from the keys JSON file

    Parameters
    ----------
    keys_filename: str (default is "keys.json")
        Filename of keys JSON

    Returns
    -------
    str
        Value of access_token from keys JSON

    """
    with open(keys_filename) as K:
        return json.load(K)["access_token"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keys", default="keys.json", help="Keys file containing auth token")
    args = parser.parse_args()
    refresh_spotify_access_token(args.keys)
