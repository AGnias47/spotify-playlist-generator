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


from sys import path
path.append("../")
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

def parse_playlist(fname, delimiter = ',') :
	"""
	Generates a list containing items of the form [artist, song]
	Input: text file name in cwd
	Output: populated list
	"""
	el = list()
	with open(fname,'r') as f :
		for line in f :
			contents = line.strip().split(delimiter)
			el.append(Track(contents[1].strip(), contents[0].strip()))
	f.close()
	return el
