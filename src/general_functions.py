#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   general_functions.py - Functions supporting use of the Spotify API
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

import json
import requests
from sys import argv as arg
from sys import exit as sys_exit


def get_json_response_dict(oauth, SearchURL) :
	"""
	Returns a json dict from a REST get request
	Input: OAuth token and Search URL
	Return Value: Json returned from request as a dict
	"""
	headers = {'Content-Type': 'application/json',
				'Authorization': 'Bearer {0}'.format(oauth)}
	response = requests.get(SearchURL, headers=headers)
	if response.status_code != 200 :
		print("catch errors here")
		return "Something bad here"
	return json.loads(response.content.decode("utf-8"))


def print_pretty_json(jsonDataLoads) :
	"""
	Prints a formatted json to stdout
	Input: json formatted as a dict by Python JSON library
	Return Value: None (prints to stdout)
	"""
	print(json.dumps(jsonDataLoads, indent=3, sort_keys=False))


if __name__ == "__main__" :
	# Used for quick testing area
	#
	# Check if the OAuth token has been defined as an argument; if not, exit
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")

