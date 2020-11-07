#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/12/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Script which returns the top search results for each track in a playlist.csv style file
"""

import argparse
from src.parse_file_into_tracks import parse_file_playlist
from spotify_token_refresh.refresh import get_access_token


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keys", default="keys.json", help="Keys file containing auth token")
    parser.add_argument("-f", "--filename", default="playlist.csv", help="File containing tracks to add to playlist")
    args = parser.parse_args()
    for track in parse_file_playlist(args.filename):
        track.view_top_results(get_access_token())
