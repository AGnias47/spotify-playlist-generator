#!/usr/bin/python3
#
#   A. Gnias
#
#   playlist_generator.py - Adds a CSV of tracks to a Spotify playlist
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0


import os
import sys
import getopt

from src.parse_file_into_tracks import parse_playlist
from src.Playlist import Playlist
from src.Exceptions import PlaylistNotInitializedError


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
    options, arguments = getopt.getopt(sys.argv[1:], "t:f:n:d:", ["token=", "filename=", "name=", "description="])
    for o, a in options:
        if o in ("-t", "--token"):
            _oauth_token = a
        elif o in ("-f", "--filename"):
            _playlist_filename = a
        elif o in ("-n", "--name"):
            _playlist_name = a
        elif o in ("-d", "--description"):
            _description = a
        else:
            print("Unhandled option; ignoring {1}", o)
    if "_oauth_token" not in locals():
        if os.path.exists("OAuth_Token"):
            with open("OAuth_Token") as T:
                _oauth_token = T.read().strip()
        else:
            _oauth_token = input("OAuth Token: ").strip()
    if "_playlist_filename" not in locals():
        _playlist_filename = input("File containing tracks to add to playlist: (playlist.csv) ").strip()
        if _playlist_filename == "":
            _playlist_filename = "playlist.csv"
    if "_playlist_name" not in locals():
        _playlist_name = input("Playlist name: (SpotifyAPI Test Playlist) ").strip()
        if _playlist_name == "":
            _playlist_name = "SpotifyAPI Test Playlist"
    if "_description" not in locals():
        _description = "Playlist generated from playlist_generator.py"
    return _oauth_token, _playlist_filename, _playlist_name, _description


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
    try:
        (
            user_oauth_token,
            playlist_fname,
            playlist_display_name,
            playlist_description,
        ) = process_commandline_parameters()
    except getopt.GetoptError as err:
        print(err, "\nExiting")
        sys.exit(1)

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
