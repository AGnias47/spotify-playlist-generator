#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import sys

sys.path.append("../")
from src.Playlist import Playlist

if len(sys.argv) > 1:
    oauth_token = sys.argv.pop()
else:
    try:
        with open("../OAuth_Token", "r") as F:
            oauth_token = F.read().strip()
        F.close()
    except FileNotFoundError:
        sys.exit("OAuth Token not provided as an argument or at ../OAuth_Token. Exiting")

TestsPassed = 0
TestsFailed = 0
P = Playlist("__TEST__")

if P.spotify_init(oauth_token):
    TestsPassed += 1
else:
    print("Playlist initialization test failed")
    TestsFailed += 1

if P.spotify_add_track(oauth_token, "0aWMVrwxPNYkKmFthzmpRi"):
    TestsPassed += 1
else:
    print("Adding track to Playlist failed")
    TestsFailed += 1

print("Tests Passed: {0}".format(TestsPassed))
print("Tests Failed: {0}".format(TestsFailed))
print("Remove __TEST__ Playlist from Spotify; no API call to do this manually as of 7/27/19\n")
