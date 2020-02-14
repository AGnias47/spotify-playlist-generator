#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/1/2019
#
#   Playlist.py - Class for interacting with Playlists
#   through the Spotify API.
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import requests
import json


class Playlist:
    def __init__(self, name="Unnamed Playlist", tracks=None, playlist_id=None):
        """
        Class to store Playlist information

        Parameters
        ----------
        name: str (default is Unnamed Playlist)
            Playlist display name
        tracks: list of Tracks (default is None)
            Tracks to be included in the playlist
        playlist_id: str (default is None)
            Spotify ID for Playlist; should be None if not yet created in Spotify
        """
        self.name = name
        self.tracks = tracks
        self.id = playlist_id
        if self.id is not None:
            self.url = "https://api.spotify.com/v1/playlists/" + self.id
        else:
            self.url = None

    def spotify_init(self, oauth, description="Playlist generated from Spotify API"):
        """
        Creates a new playlist for the logged-in user on Spotify and updates the Playlist object attributes accordingly

        Parameters
        ----------
        oauth: str
            OAuth Token retrieved from Spotify
        description: str
            Playlist description

        Returns
        -------
        bool
            True if playlist was created, else False

        """
        playlist_url = "https://api.spotify.com/v1/me/playlists"
        data = '{"name":"' + self.name + '","description":"' + description + '","public":false}'
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(oauth),
        }
        response = requests.post(playlist_url, headers=headers, data=data)
        if response.status_code != 201:
            print(f"Playlist was not created: {response.reason}")
            return False
        data = json.loads(response.content.decode("utf-8"))
        self.id = data["id"]
        self.url = data["href"]
        if self.id is not None and self.url is not None:
            return True
        else:
            return False

    def spotify_add_track(self, oauth, track_id):
        """
        Adds a track to a playlist on Spotify via the Track ID

        Parameters
        ----------
        oauth: str
            OAuth Token retrieved from Spotify
        track_id: str
            ID corresponding to track to add to Playlist

        Returns
        -------
        bool
            True upon success, else False

        """
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(oauth),
        }
        playlist_url = "https://api.spotify.com/v1/playlists/{0}/".format(self.id)
        track_ref = "tracks?uris=spotify%3Atrack%3A{0}".format(track_id)
        response = requests.post(playlist_url + track_ref, headers=headers)
        if response.status_code != 201:
            print(response.reason)
            return False
        return True
