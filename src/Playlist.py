#!/usr/bin/python3
#
#   A. Gnias
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import argv as arg
from sys import exit as sys_exit
import requests
import json


class Playlist :
	def __init__(self, name="Unnamed Playlist", tracks=None, ID=None) :
		self.name = name
		self.tracks = tracks
		self.ID = ID
		if self.ID is not None :
			self.url = set_url(ID)
		else :
			self.url = None

	def set_url(self, ID) :
		if self.ID is not None :
			self.url = "https://api.spotify.com/v1/playlists/" + self.ID
		else :
			self.url = None

	def spotify_init(self, oauth, description="Playlist generated from Spotify API") :
		"""
		Creates a new playlist for the logged-in user on Spotify
		Input: OAuth Token, Playlist name, Playlist description
		Output: True if playlist was created, else False
		"""
		PlaylistURL = "https://api.spotify.com/v1/me/playlists" 
		data = "{\"name\":\"" + self._name + "\",\"description\":\"" + description + "\",\"public\":false}" 
		headers = {'Accept': 'application/json',
					'Content-Type': 'application/json',
					'Authorization': 'Bearer {0}'.format(oauth)}
		response = requests.post(PlaylistURL, headers=headers, data=data)
		if response.status_code != 201 : 
			print(response.reason)
			return (None, None)
		data = json.loads(response.content.decode("utf-8"))
		self._id = data["id"]
		self._url = data["href"]
		if self._id is not None and self._url is not None :
			return True
		else : 
			return False

	def spotify_add_track(self, oauth, track_id) :
		"""
		Adds a track to a playlist on Spotify
		Input: OAuth Token, Playlist href, Track href
		Output: True upon success, else false
		"""
		headers = {'Accept': 'application/json',
					'Content-Type': 'application/json',
					'Authorization': 'Bearer {0}'.format(oauth)}
		PlaylistURL = "https://api.spotify.com/v1/playlists/{0}/".format(self._id)
		TrackRef = "tracks?uris=spotify%3Atrack%3A{0}".format(track_id) 
		response = requests.post(PlaylistURL + TrackRef, headers=headers)
		if response.status_code != 201 :
			print(response.reason)
			return False
		return True

if __name__ == "__main__" :
	try :
		OAUTH_token= arg[1]
	except :
		sys_exit("OAUTH token must be provided as an argument")
