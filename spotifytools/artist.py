#!/usr/bin/env python3
#
#   A. Gnias
#   Created: 7/27/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

from spotifytools.general import get_json_response_dict

"""
Class and functions utilizing the Spotify API for interacting with artist data. Performs 
more complex functionality extending beyond and unrelated to Track class.
"""


class Artist:
    def __init__(self, name, oauth=None):
        """
        Initializes an Artist object

        Parameters
        ----------
        name: str
            Artist name
        oauth: str (default is None)
            If provided, queries Spotify for Artist ID
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
    Gets Spotify data of an artist in json format

    Parameters
    ----------
    artist_name: str
        Artist's name / title
    oauth: str
        OAuth Token retrieved from Spotify

    Returns
    -------
    dict
        Contains artist data returned from Spotify API

    """
    search_base = "https://api.spotify.com/v1/search"
    search_key = f"?q={artist_name}&type=artist&market=US&limit=1"
    return get_json_response_dict(oauth, search_base + search_key)["artists"]["items"][0]


def get_artist_external_url(artist_name, oauth):
    """
    Gets the external_url for a specified artist

    Parameters
    ----------
    artist_name: str
        Artist's name / title
    oauth: str
        OAuth Token retrieved from Spotify

    Returns
    -------
    str
        External Spotify URL for artist

    """
    return query_artist(artist_name, oauth)["external_urls"]["spotify"]


def get_artist_id(artist_name, oauth):
    """
    Returns the id for a specified artist

    Parameters
    ----------
    artist_name: str
        Artist's name / title
    oauth: str
        OAuth Token retrieved from Spotify

    Returns
    -------
    str
        Spotify ID for artist

    """
    return query_artist(artist_name, oauth)["id"]


def get_album_data_by_artist(artist_id, oauth, country="US", limit=50):
    """
    Gets a list of artist's albums

    Parameters
    ----------
    artist_id: str
        Artist's name / title
    oauth: str
        OAuth Token retrieved from Spotify
    country: str (default is "US")
        Country code from within search should be executed
    limit: int (default is 50)
        Limit of albums to search; current max is 50

    Returns
    -------
    list of str
        List of album names for artist

    """
    search_url = (
        f"https://api.spotify.com/v1/artists/{artist_id}"
        f"/albums?include_groups=album,single&country={country}&limit={str(limit)}"
    )
    return [album["name"] for album in get_json_response_dict(oauth, search_url)["items"]]
