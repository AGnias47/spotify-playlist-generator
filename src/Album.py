#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/27/2019
#
#   Album.py - Class utilizing the Spotify API for
#   interacting with Album data.
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

from sys import path

path.append("../")
from src.general_functions import get_json_response_dict


class Album:
    def __init__(self, name, artist=None, year=None, album_id=None):
        """
        Initializes album class.

        Parameters
        ----------
        name: str
            Album name
        artist: str (default is None)
            Artist name
        year: int (default is None)
            Year album was released
        album_id: str (default is None)
            Spotify reference ID for album
        """
        self.name = name
        self.artist = artist
        self.year = year
        self.id = album_id
        self.tracks = None

    def set_album_metadata(self, oauth):
        """
        Searches an album and sets the object's tracks attribute

        Parameters
        ----------
        oauth: str
            OAuth Token retrieved from Spotify

        Returns
        -------
        None
            Mutates Track object by setting attributes retrieved from Spotify

        """
        self.tracks = self.get_tracks_by_album_id(oauth)
        return None

    def get_tracks_by_album_id(self, oauth):
        """
        Get data on an album's tracks

        Parameters
        ----------
        oauth: str
            OAuth Token retrieved from Spotify

        Returns
        -------
        list of Tracks

        """
        search_url = "https://api.spotify.com/v1/albums/{}/tracks".format(self.id)
        return [track[self.name] for track in get_json_response_dict(oauth, search_url)["items"]]
