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
		self._name = name
		self._tracks = tracks
		self._id = ID
		if self._id is not None :
			self._url = "https://api.spotify.com/v1/playlists/" + self._id
		else :
			self._url = None

	def name(self) :
		return self._name

	def tracks(self) :
		return self._tracks

	def id(self) :
		return self._id

	def url(self) :
		return self._url

	def set_name(self, name) :
		self._name = name

	def set_tracks(self, Tracks) :
		self._tracks = Tracks

	def set_id(self, ID) :
		self._id = ID
		if self._id is not None :
			self._url = "https://api.spotify.com/v1/playlists/" + self._id
		else :
			self._url = None

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
