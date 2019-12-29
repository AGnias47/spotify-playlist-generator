#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 7/27/2019
#
#   Album.py - Class utilizing the Spotify API for
#   interacting with Album data.
# 
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0

from sys import path
path.append("../")
from src.general_functions import get_json_response_dict


class Album:
    def __init__(self, name, artist=None, year=None, tracks=None, album_id=None):
        """
        Initializes album class.
        :param name: Album name (string)
        :param artist: Artist of album (string)
        :param year: Year album was released (int)
        :param tracks: Tracks in album (list of Track objects)
        :param album_id: Spotify album ID (string)
        """
        self.name = name
        self.artist = artist
        self.year = year
        self.tracks = tracks
        self.id = album_id

    def set_album_metadata(self, oauth):
        """
        Searches an album and sets the object's properties
        :param oauth: OAuth Token (string)
        :return: None; sets tracks attribute
        """
        self.tracks = self.get_tracks_by_album_id(oauth)
        return None

    def get_tracks_by_album_id(self, oauth):
        """
        Get data on an album's tracks. Can return data as a list of 
        either the names of an album's tracks as a string, the URL
        used to access the tracks, or the ID of the tracks.
        Input: OAuth Token, album ID, data specifier (can be either
        name, href, or id; takes name by default)
        Return value: list of specified data as strings
        """
        search_url = "https://api.spotify.com/v1/albums/{}/tracks".format(self.id)
        return [track[self.name] for track in get_json_response_dict(oauth, search_url)["items"]]
