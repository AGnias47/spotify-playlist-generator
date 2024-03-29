#!/usr/bin/python3
#
#   A. Gnias
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

import unittest

from spotifytools.track import Track


class TestTrack(unittest.TestCase):
    def setUp(self):
        self.newTrack = Track("Born to Run", "Bruce Springsteen")
        self.newSpotifyTrack = Track("Interplay", "Bill Evans", "fake/href", "fake/externalURL", "jkwon")

    def test_song(self):
        self.assertEqual(self.newTrack.song, "Born to Run")

    def test_artist(self):
        self.assertEqual(self.newTrack.artist, "Bruce Springsteen")

    def test_href(self):
        self.assertEqual(self.newSpotifyTrack.href, "fake/href")

    def test_external_url(self):
        self.assertEqual(self.newSpotifyTrack.external_url, "fake/externalURL")

    def test_id(self):
        self.assertEqual(self.newSpotifyTrack.id, "jkwon")

    def test_set_song(self):
        self.newTrack.song = "XXX"
        self.assertEqual(self.newTrack.song, "XXX")

    def test_set_artist(self):
        self.newTrack.artist = "Kendrick Lamar"
        self.assertEqual(self.newTrack.artist, "Kendrick Lamar")

    def test_set_href(self):
        self.newTrack.href = "href/Bruce"
        self.assertEqual(self.newTrack.href, "href/Bruce")

    def test_set_id(self):
        self.newTrack.id = "idBruce"
        self.assertEqual(self.newTrack.id, "idBruce")

    def test_set_external_url(self):
        self.newSpotifyTrack.external_url = "fake/morefake/externalURL"
        self.assertEqual(self.newSpotifyTrack.external_url, "fake/morefake/externalURL")


if __name__ == "__main__":
    unittest.main()
