#!/usr/bin/python3
#
#   A. Gnias
#
#   playlist_generator.py - Adds a CSV of tracks to a Spotify playlist
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0


import os
import sys
import getopt

from src.parse_file_into_tracks import *
from src.Playlist import Playlist


def process_commandline_parameters():
    """
    Processes commandline parameters
    Input: None (hard-coded with the function)
    Output: Tuple containing o_auth_token (string), playlist_filename (string), playlist_name (string),
    description (string)
    """
    try:
        options, arguments = getopt.getopt(sys.argv[1:], "t:f:n:d:", ["token=", "filename=", "name=", "description="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(1)
    for o, a in options:
        if o in ("-t", "--token"):
            o_auth_token = a
        elif o in ("-f", "--filename"):
            playlist_filename = a
        elif o in ("-n", "--name"):
            playlist_name = a
        elif o in ("-d", "--description"):
            description = a
        else:
            print("Unhandled option; ignoring {1}", o)
    if "o_auth_token" not in locals():
        if os.path.exists("o_auth_token"):
            with open("o_auth_token") as T:
                o_auth_token = T.read().strip()
        else:
            o_auth_token = input("OAuth Token: ").strip()
    if "playlist_filename" not in locals():
        playlist_filename = input("File containing tracks to add to playlist: (playlist.csv) ").strip()
        if playlist_filename == "":
            playlist_filename = "playlist.csv"
    if "playlist_name" not in locals():
        playlist_name = input("Playlist name: (SpotifyAPI Test Playlist) ").strip()
        if playlist_name == "":
            playlist_name = "SpotifyAPI Test Playlist"
    if "description" not in locals():
        description = "Playlist generated from playlist_generator.py"
    return o_auth_token, playlist_filename, playlist_name, description


def create_playlist_and_add_tracks_from_file():
    """
    Creates playlist in Spotify for a user and adds tracks from file into the playlist
    :return: List of tracks unable to be added to the playlist, or exit before completion if fatal error occurs
    """
    (oauth_token, playlist_filename, playlist_name, description) = process_commandline_parameters()

    # Parse the tracks from the CSV; CSV of the form (artist, song name)
    playlist_tracks = parse_playlist(playlist_filename)
    if not playlist_tracks:
        sys.exit(f"{playlist_tracks} either does not exist or does not have any content; exiting")

    # Initialize the Playlist to be created in the user's Spotify Library
    playlist = Playlist(playlist_name, playlist_tracks)
    if not playlist.spotify_init(oauth_token, description):
        sys.exit("Playlist could not be created; exiting")

    # Add the tracks from the CSV to the Playlist
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
    missed_tracks_list = create_playlist_and_add_tracks_from_file()
    if missed_tracks_list:
        print("\nTracks unable to be found: ")
        print(*missed_tracks_list, sep="\n")
    else:
        print("\nAll tracks added successfully\n")
