#!/usr/bin/python3
#
#   A. Gnias
#
#   track_searcher.py - Gives top results of a list of tracks
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0

import sys
sys.path.append("./src")
from src.parse_file_into_tracks import *


# Check if the OAUTH_token was provided as an argument
if len(sys.argv) > 1:
    oauth_token = sys.argv.pop()
else:
    try:
        with open("OAuth_Token", 'r') as F:
            oauth_token = F.read().strip()
    except FileNotFoundError:
        sys.exit("OAuth Token not provided as an argument or at OAuth_Token. Exiting")


# Parse the tracks from the CSV
for track in parse_playlist("functional_test/Test_Artifacts/playlist.csv") :
    track.view_top_results(oauth_token)
