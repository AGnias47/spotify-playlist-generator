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
from fuzzywuzzy import fuzz as fuzzy


def get_artist_JSON_test(OAUTH_token, artist) :
	sleep(test_delay)

if len(arg) > 1 :
	OAuth_Token = arg.pop()
else :
	try :
		with open("../OAuth_Token", 'r') as F :
			OAuth_Token = F.read().strip()
		F.closed
	except :
		exit("OAuth Token not provided as an argument or at ../OAuth_Token. Exiting")

TestsPassed = 0
TestsFailed = 0

# print_pretty_json test
artist = Artist("Seal", OAuth_Token)
with open("Test_Artifacts/functional.json",'a') as F:
	with redirect_stdout(F):
		print_pretty_json(artist.query_artist(OAuth_Token)) #print this to file and compare
F.closed
with open("Test_Artifacts/seal.json", 'r') as S :
	expected = S.read().strip()
S.closed
with open("Test_Artifacts/functional.json", 'r') as T :
	actual = T.read().strip()
T.closed
if fuzzy.ratio(expected, actual) > 95 :
	TestsPassed += 1
else :
	print("print_pretty_json test failed")
	TestsFailed += 1

# get_json_response_dict test
# basically what the print function does, just allows us to show dict functionality in more than one way
SearchBase = "https://api.spotify.com/v1/search"
SearchKey = "?q={0}&type=artist&market=US&limit=1".format("Seal")
raw_d = get_json_response_dict(OAuth_Token, SearchBase + SearchKey)
d = raw_d["artists"]["items"][0]
e_href = "https://api.spotify.com/v1/artists/5GtMEZEeFFsuHY8ad4kOxv"
e_id = "5GtMEZEeFFsuHY8ad4kOxv"
e_name = "Seal"
e_type = "artist"
if e_href == d["href"] and e_id == d["id"] and e_name == d["name"] and e_type == d["type"] :
	TestsPassed += 1
else :
	print("get_json_response_dict test failed")
	TestsFailed += 1

# Cleanup and print results
remove("Test_Artifacts/functional.json")
print("Tests Passed: {0}".format(TestsPassed))
print("Tests Failed: {0}\n".format(TestsFailed))
