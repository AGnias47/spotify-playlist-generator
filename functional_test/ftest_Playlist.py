#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("../")
from src.Playlist import Playlist
from src.Track import Track
import unittest
from sys import argv as arg

if len(arg) > 1 :
	OAuth_Token = arg.pop()
else :
	try :
		with open("../OAuth_Token", 'r') as F :
			OAuth_Token = F.read().strip()
		F.close()
	except :
		exit("OAuth Token not provided as an argument or at ../OAuth_Token. Exiting")

TestsPassed = 0
TestsFailed = 0
P = Playlist("__TEST__")

if P.spotify_init(OAuth_Token) == True :
	TestsPassed += 1
else :
	print("Playlist initialization test failed")
	TestsFailed += 1

if P.spotify_add_track(OAuth_Token, "0aWMVrwxPNYkKmFthzmpRi") == True :
	TestsPassed += 1
else :
	print("Adding track to Playlist failed")
	TestsFailed += 1

print("Tests Passed: {0}".format(TestsPassed))
print("Tests Failed: {0}".format(TestsFailed))
print("Remove __TEST__ Playlist from Spotify; no API call to do this manually as of 7/27/19\n")
