#!/usr/bin/python3
#
#   A. Gnias
#   Created: ~7/18/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Adds a CSV of tracks to a Spotify playlist
"""

import sys
import argparse
from json import JSONDecodeError

from spotifytools.parser import parse_file_playlist
from spotifytools.playlist import Playlist
from spotifytools.exceptions import PlaylistNotInitializedError
from spotifytools.token_refresh import get_access_token


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keys", default="keys.json", help="Keys file containing auth token")
    parser.add_argument("-f", "--filename", default="playlist.csv", help="File containing tracks to add to playlist")
    parser.add_argument("-n", "--name", default="SpotifyAPI Test Playlist", help="Playlist name")
    parser.add_argument(
        "-d", "--description", default="Playlist generated from playlist_generator.py", help="Playlist description"
    )
    args = parser.parse_args()
    keys_filename, playlist_fname, playlist_display_name, playlist_description = (
        args.keys,
        args.filename,
        args.name,
        args.description,
    )
    user_oauth_token = get_access_token(keys_filename)
    playlist_tracks = parse_file_playlist(playlist_fname)

    print(f'Creating the playlist "{playlist_display_name}"')
    playlist = Playlist(playlist_display_name, playlist_tracks)
    playlist.spotify_init(user_oauth_token, playlist_description)

    print(f"Adding songs from {playlist_fname} to {playlist_display_name}")
    added_tracks_list, missed_tracks_list = playlist.spotify_add_tracks(user_oauth_token)

    if missed_tracks_list:
        print("\nTracks unable to be found: ")
        print(*missed_tracks_list, sep="\n")
    else:
        print("\nAll tracks added successfully\n")
