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
artist = "Seal"
print_pretty_json(query_artist(OAUTH_token, artist)) #print this to file and compare

print("Tests Passed: {0}".format(TestsPassed))
print("Tests Failed: {0}".format(TestsFailed))
