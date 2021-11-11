#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/1/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Class for interacting with Playlists through the Spotify API
"""

import json
import requests
from spotifytools.exceptions import PlaylistNotInitializedError

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

        Raises
        -------
        PlaylistNotInitializedError
            Raised if Playlist cannot be created in Spotify

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
            "Authorization": f"Bearer {oauth}"
        }
        response = requests.post(playlist_url, headers=headers, data=data)
        if response.status_code != 201:
            raise PlaylistNotInitializedError(response.reason)
        data = json.loads(response.content.decode("utf-8"))
        self.id = data["id"]
        self.url = data["href"]
        # If ID and URL are not properly returned by playlist creation call, return false
        if self.id is None or self.url is None:
            return False
        return True

    def spotify_add_track(self, oauth, track_id, quiet=False):
        """
        Adds a track to a playlist on Spotify via the Track ID

        Parameters
        ----------
        oauth: str
            OAuth Token retrieved from Spotify
        track_id: str
            ID corresponding to track to add to Playlist
        quiet: bool (default is False)
            If true, suppress output; no functional difference

        Returns
        -------
        bool
            True upon success, else False

        """
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {oauth}",
        }
        playlist_url = f"https://api.spotify.com/v1/playlists/{self.id}/"
        track_ref = f"tracks?uris=spotify%3Atrack%3A{track_id}"
        response = requests.post(playlist_url + track_ref, headers=headers)
        if response.status_code != 201:
            if not quiet:
                print(response.reason)
            return False
        return True

    def spotify_add_tracks(self, oauth_token, quiet=False):
        """
        Adds tracks in self.tracks to the playlist in Spotify.
        If any tracks are missed, append them to the missed_tracks list


        Parameters
        ----------
        oauth_token: str
            OAuth Token retrieved from Spotify
        quiet: bool (default is False)
            If true, suppress output; no functional difference


        Returns
        -------
        list(Tracks)
            List includes Tracks unable to be added to the playlist

        """
        added_tracks, missed_tracks = list(), list()
        for track in self.tracks:
            if not quiet:
                print(f"Adding {track.song} by {track.artist}")
            # If track was found via search, add to playlist
            if track.spotify_query(oauth_token):
                # If the track was not added, append to missed_tracks, else continue
                if self.spotify_add_track(oauth_token, track.id):
                    added_tracks.append(track.song + " by " + track.artist)
                else:
                    missed_tracks.append(track.song + " by " + track.artist)
            # If track was not found via search, append to missed_tracks
            else:
                missed_tracks.append(track.song + ", " + track.artist)
        return added_tracks, missed_tracks
