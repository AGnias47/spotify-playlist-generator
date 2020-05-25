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

from src.parse_file_into_tracks import parse_playlist
from src.Playlist import Playlist
from src.Exceptions import PlaylistNotInitializedError
from spotify_token_refresh.refresh import get_access_token


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
    try:
        user_oauth_token = get_access_token(keys_filename)
    except FileNotFoundError:
        sys.exit(f'Path to file "{keys_filename}" either does not exist; Exiting')
    except JSONDecodeError as e:
        sys.exit(f'{keys_filename}" must be a valid json: \nError: {e}')
    try:
        playlist_tracks = parse_playlist(playlist_fname)
    except FileNotFoundError:
        sys.exit(f'Path to file "{playlist_fname}" does not exist or does not have any content; Exiting')

    print(f'Creating the playlist "{playlist_display_name}"')
    playlist = Playlist(playlist_display_name, playlist_tracks)
    try:
        if not playlist.spotify_init(user_oauth_token, playlist_description):
            raise PlaylistNotInitializedError
    except PlaylistNotInitializedError as e:
        sys.exit(f"Could not create playlist in Spotify; Exiting.\nError: {e}")

    print(f"Adding songs from {playlist_fname} to {playlist_display_name}")
    missed_tracks_list = playlist.spotify_add_tracks(user_oauth_token)
    if missed_tracks_list:
        print("\nTracks unable to be found: ")
        print(*missed_tracks_list, sep="\n")
    else:
        print("\nAll tracks added successfully\n")
