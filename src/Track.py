#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/1/2019
#
#   Track.py - Class for interacting with Tracks through
#   the Spotify API.
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]

from sys import path

path.append("../")
from src.general_functions import get_json_response_dict
from fuzzywuzzy import fuzz as fuzzy


class Track:
    def __init__(self, song, artist, href=None, external_url=None, track_id=None):
        """
        Stores Track Data
        :param song: Track name (string)
        :param artist: Track artist (string)
        :param href: Spotify track href (string url)
        :param external_url: Spotify track external url (string url)
        :param track_id: Spotify track id (string)
        """
        self.artist = artist
        self.song = song
        self.href = href
        self.external_url = external_url
        self.id = track_id

    def spotify_query(self, oauth, lev_partial_ratio=75, market="US", limit=10):
        """
        Finds a track via a Spotify search
        :param oauth: OAuth Token as a string
        :param lev_partial_ratio: Levenshtein distance ratio
        :param market: Country market; US by default
        :param limit: Search Limit; Max and default is 10 as of v1
        :return: True if track is found, else False; mutates Track object with Spotify data if found
        """
        search_base = "https://api.spotify.com/v1/search"
        search_key = "?q={0}&type=track&market={1}&limit={2}".format(self.song, market, limit)
        search_items = get_json_response_dict(oauth, search_base + search_key)["tracks"]["items"]
        for item in search_items:
            artist = item["artists"][0]["name"]
            song = item["name"]
            if (
                fuzzy.partial_ratio(artist.lower(), self.artist.lower()) > lev_partial_ratio
                and fuzzy.partial_ratio(song.lower(), self.song.lower()) > lev_partial_ratio
            ):
                self.href = item["href"]
                self.external_url = item["external_urls"]["spotify"]
                self.id = item["id"]
                return True
        return False

    def view_top_results(self, oauth, market="US", limit=10):
        """
        Prints a track's top search results from a Spotify query
        :param oauth: OAuth Token as a string
        :param market: Country market; US by default
        :param limit: Search Limit; Max and default is 10 as of v1
        :return: None
        """
        search_base = "https://api.spotify.com/v1/search"
        search_key = "?q={0}&type=track&market={1}&limit={2}".format(self.song, market, limit)
        search_items = get_json_response_dict(oauth, search_base + search_key)["tracks"]["items"]
        result = 1
        for item in search_items:
            artist = item["artists"][0]["name"]
            song = item["name"]
            album = item["album"]["name"]
            print("{0}. {1}".format(result, song))
            print("   " + artist)
            print("   " + album + "\n")
            result += 1
        return None
