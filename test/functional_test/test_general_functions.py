#!/usr/bin/python3
#
#   A. Gnias
#   Created: 7/30/2019
#
#   test_general_functions.py - Functional test of general functions
#
#   Requirements: OAuth Token value for Spotify API
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

import os
from contextlib import redirect_stdout
import unittest

from fuzzywuzzy import fuzz as fuzzy

from src.general_functions import *
from src.Artist import Artist, query_artist
from spotify_token_refresh.refresh import get_access_token


class Seal:
    """
    Defines expected attributes of the artist Seal within Spotify
    """

    def __init__(self):
        self.name = "Seal"
        self.type = "artist"
        self.href = "https://api.spotify.com/v1/artists/5GtMEZEeFFsuHY8ad4kOxv"
        self.spotify_id = "5GtMEZEeFFsuHY8ad4kOxv"


class GeneralFunctionTests(unittest.TestCase):
    def setUp(self):
        self.access_token = get_access_token()
        self.artist = Seal()
        self.artist_json = "test/test_artifacts/seal.json"
        self.prettyprint_json_filename = "test/test_artifacts/functional.json"
        self.search_url = "https://api.spotify.com/v1/search"
        self.search_key = f"?q={self.artist.name}&type=artist&market=US&limit=1"

    def test_print_pretty_json(self):
        """

        Returns
        -------

        """
        artist = Artist(self.artist.name, self.access_token)
        with open(self.prettyprint_json_filename, "w") as F:
            with redirect_stdout(F):
                print_pretty_json(query_artist(artist.name, self.access_token))  # print this to file and compare
        with open(self.artist_json, "r") as S:
            expected = S.read().strip()
        with open(self.prettyprint_json_filename, "r") as T:
            actual = T.read().strip()
        assert fuzzy.ratio(expected, actual) > 95
        # Need this in like a finally function
        os.remove(self.prettyprint_json_filename)

    def test_get_json_response_dict(self):
        """
        basically what the print function does, just allows us to show dict functionality in more than one way

        Returns
        -------

        """
        raw_d = get_json_response_dict(self.access_token, self.search_url + self.search_key)
        d = raw_d["artists"]["items"][0]
        self.assertEqual(self.artist.name, d["name"])
        self.assertEqual(self.artist.type, d["type"])
        self.assertEqual(self.artist.href, d["href"])
        self.assertEqual(self.artist.spotify_id, d["id"])
