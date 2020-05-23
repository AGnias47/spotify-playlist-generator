#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/1/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Class for interacting with Tracks through the Spotify API
"""

from src.general_functions import get_json_response_dict
from fuzzywuzzy import fuzz as fuzzy


class Track:
    def __init__(self, song, artist, href=None, external_url=None, track_id=None):
        """
        Initializes Track class for storing Spotify track data

        Parameters
        ----------
        song: str
            Track name
        artist: str
            Track artist
        href: str (default is None)
            URL referring to Track in Spotify
        external_url: str (default is None)
            external URL referring to Track in Spotify
        track_id: str (default is None)
            ID referring to Track in Spotify
        """
        self.artist = artist
        self.song = song
        self.href = href
        self.external_url = external_url
        self.id = track_id

    def spotify_query(self, oauth, lev_partial_ratio=75, market="US", limit=10):
        """
        Finds a track via a Spotify search

        Parameters
        ----------
        oauth: str
            OAuth Token retrieved from Spotify
        lev_partial_ratio: int [0-100]
            Levenshtein distance ratio
        market: str (default is "US")
            Country market
        limit: int (default is 10)
            Limit of tracks to query; max is 10 as of v1 of API

        Returns
        -------
        bool
            True if track is found, else False; mutates Track object with Spotify data if found

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

        Parameters
        ----------
        oauth: str
            OAuth Token retrieved from Spotify
        market: str (default is "US")
            Country market
        limit: int (default is 10)
            Limit of tracks to query; max is 10 as of v1 of API

        Returns
        -------
        None
            Prints results to stdout

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
