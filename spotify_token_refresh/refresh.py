#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.7.5
#   Vim 8.1

import requests
import json
from base64 import b64encode


def refresh_spotify_access_token(keys_filename, output_file=None):
    """
    Refreshes the access token in a json file with the contents:

    ```json
    {
        "client_id": "client id",
        "client_secret": "client secret",
        "access_token": "access token",
        "refresh_token": "refresh token"
    }
    ```

    Parameters
    ----------
    keys_filename: str
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
    with open(keys_filename) as K:
        return json.load(K)["access_token"]


if __name__ == "__main__":
    refresh_spotify_access_token("keys.json")  # Eventually parameterize keys.json
