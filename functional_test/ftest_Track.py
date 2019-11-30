#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0

import sys
sys.path.append("../")
from src.Track import Track

if len(sys.argv) > 1:
    OAuth_Token = sys.argv.pop()
else:
    try:
        with open("../OAuth_Token", 'r') as F:
            OAuth_Token = F.read().strip()
        F.close()
    except FileNotFoundError:
        sys.exit("OAuth Token not provided as an argument or at ../OAuth_Token. Exiting")

TestsPassed = 0
TestsFailed = 0
T = Track("Blue in Green", "Miles Davis")

if T.spotify_query(OAuth_Token):
    TestsPassed += 1
else:
    print("Spotify track query test failed")
    TestsFailed += 1

print("Tests Passed: {0}".format(TestsPassed))
print("Tests Failed: {0}\n".format(TestsFailed))
