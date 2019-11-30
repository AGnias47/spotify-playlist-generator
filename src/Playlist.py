#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/1/2019
#
#   Playlist.py - Class for interacting with Playlists
#   through the Spotify API.
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

import requests
import json


class Playlist:
    def __init__(self, name="Unnamed Playlist", tracks=None, playlist_id=None):
        self.name = name
        self.tracks = tracks
        self.id = playlist_id
        if self.id is not None:
            self.url = "https://api.spotify.com/v1/playlists/" + self.id
        else:
            self.url = None

    def spotify_init(self, oauth, description="Playlist generated from Spotify API") :
        """
        Creates a new playlist for the logged-in user on Spotify
        Input: OAuth Token, Playlist name, Playlist description
        Output: True if playlist was created, else False
        """
        playlist_url = "https://api.spotify.com/v1/me/playlists"
        data = "{\"name\":\"" + self.name + "\",\"description\":\"" + description + "\",\"public\":false}" 
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(oauth)}
        response = requests.post(playlist_url, headers=headers, data=data)
        if response.status_code != 201:
            print(response.reason)
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
        Adds a track to a playlist on Spotify
        Input: OAuth Token, Playlist href, Track href
        Output: True upon success, else false
        """
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(oauth)}
        playlist_url = "https://api.spotify.com/v1/playlists/{0}/".format(self.id)
        track_ref = "tracks?uris=spotify%3Atrack%3A{0}".format(track_id)
        response = requests.post(playlist_url + track_ref, headers=headers)
        if response.status_code != 201:
            print(response.reason)
            return False
        return True
