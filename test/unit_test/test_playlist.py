#!/usr/bin/python3
#
#   A. Gnias
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

import unittest

from spotifytools.playlist import Playlist
from spotifytools.track import Track


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.newPlaylist = Playlist("A new playlist test instance")

    def test_name(self):
        self.assertEqual(self.newPlaylist.name, "A new playlist test instance")

    def test_id(self):
        self.assertEqual(self.newPlaylist.id, None)

    def test_tracks(self):
        self.assertEqual(self.newPlaylist.tracks, None)

    def test_url(self):
        if self.newPlaylist.id is not None:
            self.assertEqual(self.newPlaylist.url, "https://api.spotify.com/v1/playlists/" + self.newPlaylist.id)
        else:
            self.assertEqual(self.newPlaylist.url, None)

    def test_set_name(self):
        self.newPlaylist.name = "Playlist Name Change"
        self.assertEqual(self.newPlaylist.name, "Playlist Name Change")

    def test_set_id(self):
        self.newPlaylist.id = "00001"
        self.assertEqual(self.newPlaylist.id, "00001")

    def test_set_tracks(self):
        self.newPlaylist.track = Track("EARFQUAKE", "Tyler, The Creator")
        self.assertEqual(self.newPlaylist.track.song, "EARFQUAKE")
        self.assertEqual(self.newPlaylist.track.artist, "Tyler, The Creator")


if __name__ == "__main__":
    unittest.main()
