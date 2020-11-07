#!/usr/bin/env python3
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

import json
from random import randint
import urllib.parse

from flask import Flask, render_template, Response, request, redirect, url_for

from src.parse_file_into_tracks import parse_file_playlist
from src.Playlist import Playlist
from src.Exceptions import PlaylistNotInitializedError
from spotify_token_refresh.refresh import get_access_token


app = Flask(__name__)

with open("keys.json") as K:
    keys = json.load(K)


@app.route("/login", methods=["GET", "POST"])
def login():
    client_id = keys["client_id"]
    state = generate_random_string(16)
    scope = "user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public"
    redirect_uri = "http://localhost:5000/callback"
    url = "https://accounts.spotify.com/authorize?"
    url += f"response_type=code&client_id={client_id}"
    url += f"&scope={scope}&redirect_uri={redirect_uri}&state={state}"
    return redirect(url)


@app.route("/callback")
def callback():
    try:
        return request.args.keys()
    except:
        try:
            return request.form.keys()
        except:
            return "A"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def submit_form():
    playlist_name = request.form["name"]
    playlist_description = request.form["desc"]
    user_oauth_token = request.form["apikey"]
    playlist_content = request.form["playlist-content"]
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def create_playlist():
    playlist_name = request.form["name"]
    playlist_description = request.form["desc"]
    user_oauth_token = request.form["apikey"]
    playlist_content = request.form["playlist-content"]
    # create_playlist_help(playlist_name, playlist_content, user_oauth_token,playlist_description)
    return render_template("submit.html", playlist_name=playlist_name, playlist_description=playlist_description, playlist_content=playlist_content)


def generate_random_string(length):
    text = str()
    for i in range(0, length):
        text += get_random_character()
    return text


def get_random_character():
    random_ascii_chars = [[65, 90], [97, 122], [48, 57]]
    rand_type = random_ascii_chars[randint(0, len(random_ascii_chars) - 1)]
    return chr(randint(rand_type[0], rand_type[1]))


def create_playlist_help(
    playlist_display_name, playlist_tracks, user_oauth_token, playlist_description
):
    playlist = Playlist(playlist_display_name, playlist_tracks)
    if not playlist.spotify_init(user_oauth_token, playlist_description):
        raise PlaylistNotInitializedError
    missed_tracks_list = playlist.spotify_add_tracks(user_oauth_token)
