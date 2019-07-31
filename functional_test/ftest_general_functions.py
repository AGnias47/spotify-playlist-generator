#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 7/30/2019
#
#   ftest_general_functions.py - Functional test of general functions
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path
path.append("../")
from src.general_functions import *
from filecmp import cmp
from sys import argv as arg, exit
from contextlib import redirect_stdout
from src.Artist import Artist
from os import remove


def get_artist_JSON_test(OAUTH_token, artist) :
	sleep(test_delay)

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

# Artist to use as an example
artist = Artist("Seal", OAuth_Token)
with open("Test_Artifacts/functional.json",'a') as F:
	with redirect_stdout(F):
		print_pretty_json(artist.query_artist(OAuth_Token)) #print this to file and compare
F.closed
try : 
	assert cmp("Test_Artifacts/seal.json", "Test_Artifacts/functional.json")
	TestsPassed += 1
except :
	TestsFailed += 1
finally :
	remove("Test_Artifacts/functional.json")
	print("Tests Passed: {0}".format(TestsPassed))
	print("Tests Failed: {0}".format(TestsFailed))
