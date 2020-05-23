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

from src.parse_file_into_tracks import parse_playlist
from src.Playlist import Playlist
from src.Exceptions import PlaylistNotInitializedError
from spotify_token_refresh.refresh import get_access_token


def process_commandline_parameters():
    """
    Processes commandline parameters hard-coded within the function

    Parameters
    -------
    N/A

    Returns
    -------
    tuple
        Contains:
            OAuth Token: str
            Playlist Filename: str
            Playlist Display Name: str
            Playlist Description: str

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keys", default="keys.json", help="Keys file containing auth token")
    parser.add_argument("-f", "--filename", default="playlist.csv", help="File containing tracks to add to playlist")
    parser.add_argument("-n", "--name", default="SpotifyAPI Test Playlist", help="Playlist name")
    parser.add_argument(
        "-d", "--description", default="Playlist generated from playlist_generator.py", help="Playlist description"
    )
    args = parser.parse_args()
    return args.keys, args.filename, args.name, args.description


def create_playlist_and_add_tracks_from_file(oauth_token, playlist_filename, playlist_name, description):
    """
    Creates playlist in Spotify for a user and adds tracks from file into the playlist

    Parameters
    ----------
    oauth_token: str
        OAuth Token retrieved from Spotify
    playlist_filename: str
        Filepath to playlist
    playlist_name: str
        Name of playlist
    description: str
        Playlist description

    Raises
    -------
    PlaylistNotInitializedError
        Raised if Playlist cannot be created in Spotify

    Returns
    -------
    list of Tracks
        List includes Tracks unable to be added to the playlist

    """
    # Parse the tracks from the CSV; CSV is of the form (artist, song name)
    playlist_tracks = parse_playlist(playlist_filename)
    # Initialize the Playlist to be created in the user's Spotify Library
    playlist = Playlist(playlist_name, playlist_tracks)
    if not playlist.spotify_init(oauth_token, description):
        raise PlaylistNotInitializedError
    # Add the tracks from the CSV to the Playlist; if any are not added, append them to the missed_tracks list
    missed_tracks = list()
    print(f"Adding songs from {playlist_filename} to {playlist.name}")
    for track in playlist_tracks:
        print(f"Adding {track.song} by {track.artist}")
        if track.spotify_query(oauth_token):  # If track was found via search
            if not playlist.spotify_add_track(oauth_token, track.id):  # add to playlist
                missed_tracks.append(track.song + ", " + track.artist)
        else:
            missed_tracks.append(track.song + ", " + track.artist)
    return missed_tracks


if __name__ == "__main__":
    (keys_filename, playlist_fname, playlist_display_name, playlist_description,) = process_commandline_parameters()
    user_oauth_token = get_access_token(keys_filename)
    try:
        missed_tracks_list = create_playlist_and_add_tracks_from_file(
            user_oauth_token, playlist_fname, playlist_display_name, playlist_description
        )
    except FileNotFoundError:
        sys.exit(f'Path to file "{playlist_fname}" either does not exist or does not have any content; Exiting')
    except PlaylistNotInitializedError:
        sys.exit("Playlist could not be created in Spotify; exiting")
    if missed_tracks_list:
        print("\nTracks unable to be found: ")
        print(*missed_tracks_list, sep="\n")
    else:
        print("\nAll tracks added successfully\n")
