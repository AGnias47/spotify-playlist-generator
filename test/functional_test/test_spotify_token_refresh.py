#!/usr/bin/env python3
#
#   A. Gnias
#   Created: 5/2/2020
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Tests spotify_token_refresh module
"""

import unittest
import os
import hashlib
import json
from spotifytools.token_refresh import refresh_spotify_access_token, get_access_token
from spotifytools.general import get_json_response_dict


keys = "keys.json"


class TestSpotifyTokenRefresh(unittest.TestCase):
    def setUp(self):
        self.test_keys = "test/test_artifacts/test_keys.json"
        self.test_access_token = "accesstokenvalue"
        self.keys = keys
        self.search_example = "https://api.spotify.com/v1/search?q=Ahmad%20Jamal&type=artist&market=US&limit=1"
        with open("test/test_artifacts/ahmad_jamal_search_result") as A:
            self.search_content = json.load(A)

    def test_get_access_token(self):
        self.assertEqual(get_access_token(self.test_keys), self.test_access_token)

    @unittest.skipUnless(os.path.exists(keys), "Actual keys.json needed to run full test")
    def test_refresh_spotify_access_token(self):
        m = hashlib.sha3_256()
        with open(self.keys, "rb") as F:
            buffer = F.read()
            m.update(buffer)
        initial_hash = m.digest()
        refresh_spotify_access_token()
        with open(self.keys, "rb") as F:
            buffer = F.read()
            m.update(buffer)
        new_hash = m.digest()
        self.assertNotEqual(initial_hash, new_hash)
        self.assertEqual(
            get_json_response_dict(get_access_token(), self.search_example)["artists"]["href"],
            self.search_content["artists"]["href"],
        )
