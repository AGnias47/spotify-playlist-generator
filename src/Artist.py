#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 7/27/2019
#
#   Artist.py - Class utilizing the Spotify API for
#   interacting with artist data. Performs
#   more complex functionality extending
#   beyond and unrelated to Track class.
# 
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0

from sys import path
path.append("../")
from src.general_functions import get_json_response_dict


class Artist:
    def __init__(self, name, oauth=None):
        """
        Initializes an Artist object
        :param name: Artist name (string)
        :param oauth: OAuth Token (string, or None)
        """
        self.name = name
        if oauth is None:
            self.external_url = None
            self.id = None
        else:
            self.external_url = get_artist_external_url(self.name, oauth)
            self.id = get_artist_id(self.name, oauth)


def query_artist(artist_name, oauth):
    """
    Returns Spotify data of an artist in json format
    Input: OAUTH token as a string, artist as a string
    Return Value: Artist data as a dict
    """
    search_base = "https://api.spotify.com/v1/search"
    search_key = "?q={0}&type=artist&market=US&limit=1".format(artist_name)
    return get_json_response_dict(oauth, search_base + search_key)["artists"]["items"][0]


def get_artist_external_url(artist_name, oauth):
    """
    Returns the external_url for a specified artist
    Input: OAUTH token as a string, artist as a string
    Return Value: external_url as a string
    """
    return query_artist(artist_name, oauth)["external_urls"]["spotify"]


def get_artist_id(artist_name, oauth):
    """
    Returns the id for a specified artist
    Input: OAUTH token as a string, artist as a string
    Return Value: id as a string
    """
    return query_artist(artist_name, oauth)["id"]


def get_album_data_by_artist(artist_id, oauth, country="US", limit=50):
    """
    Get data on an artists albums. Can return data as a list of
    either the names of an artist's albums as a string, the URL
    used to access the albums, or the ID of the albums. Returns
    list of names in current iteration.
    Input: OAuth Token, artist ID, data specifier (can be either
    name, href, or id; takes name by default)
    Return value: list of specified data as strings
    """
    search_url = f"https://api.spotify.com/v1/artists/{artist_id}" \
                 f"/albums?include_groups=album,single&country={country}&limit={str(limit)}"
    return [album["name"] for album in get_json_response_dict(oauth, search_url)["items"]]
