#!/usr/bin/python3
#
#   A. Gnias
#   Created: ~7/18/2019
#
#   5.4.0-32-generic #36-Ubuntu
#   Python 3.8.2
#   Vim 8.1

"""
Adds a CSV of tracks to a Spotify playlist
"""

import sys
import argparse
from json import JSONDecodeError

from flask import Flask, render_template, Response, request, redirect, url_for

from src.parse_file_into_tracks import parse_playlist
from src.Playlist import Playlist
from src.Exceptions import PlaylistNotInitializedError
from spotify_token_refresh.refresh import get_access_token



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/", methods=["POST"])
def submit_form():
    playlist_name = request.form["name"]
    playlist_description = request.form["desc"]
    user_oauth_token = request.form["apikey"]
    playlist_content = request.form["playlist-content"]
    return render_template('index.html')
    

@app.route("/submit/", methods=['POST'])
def create_playlist():
    playlist_name = None
    playlist_tracks = None
    user_oauth_token = None
    playlist_description = None
    playlist = Playlist(playlist_display_name, playlist_tracks)
    if not playlist.spotify_init(user_oauth_token, playlist_description):
        raise PlaylistNotInitializedError
    missed_tracks_list = playlist.spotify_add_tracks(user_oauth_token)

