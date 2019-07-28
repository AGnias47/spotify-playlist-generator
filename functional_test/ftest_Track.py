#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("../")
from src.Track import Track
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
T = Track("Blue in Green", "Miles Davis")

if T.spotify_query(OAuth_Token) == True :
	TestsPassed += 1
else :
	TestsFailed += 1

print("Tests Passed: {0}".format(TestsPassed))
print("Tests Failed: {0}".format(TestsFailed))
