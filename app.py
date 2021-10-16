#!/usr/bin/env python3

"""
Flask app for generating a Spotify playlist from text
"""

import base64
import json
import urllib.parse

from flask import Flask, render_template, request, redirect, session
import requests

from spotifytools.general import generate_random_string
from spotifytools.parser import parse_string_playlist
from spotifytools.playlist import Playlist
from spotifytools.exceptions import PlaylistNotInitializedError, UnsuccessfulGetRequest


app = Flask(__name__)
app.secret_key = generate_random_string(77)
with open("keys.json") as K:
    keys = json.load(K)


@app.route("/", methods=["GET", "POST"])
def login():
    client_id = keys["client_id"]
    state = generate_random_string(16)
    scope = "user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public"
    redirect_uri = "http://localhost:5000/callback"
    url = "https://accounts.spotify.com/authorize?"
    url += f"response_type=code&client_id={client_id}"
    url += f"&scope={urllib.parse.quote(scope)}&redirect_uri={urllib.parse.quote(redirect_uri)}&state={state}"
    return redirect(url)


@app.route("/callback")
def callback():
    client_id = keys["client_id"]
    secret_id = keys["client_secret"]
    authorization_code = request.args["code"]
    encoded_auth = base64.urlsafe_b64encode(f"{client_id}:{secret_id}".encode("UTF-8")).decode("UTF-8")
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {encoded_auth}"}
    params = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": "http://localhost:5000/callback",
    }
    response = requests.post("https://accounts.spotify.com/api/token/", headers=headers, params=params)
    session["OAUTH_TOKEN"] = json.loads(response.content)["access_token"]
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def create_playlist():
    playlist_name = request.form["name"]
    playlist_description = request.form["desc"]
    if request.form["delimiter"] == "dash":
        delimiter = "-"
    elif request.form["delimiter"] == "slash":
        delimiter = "/"
    elif request.form["delimiter"] == "comma":
        delimiter = ","
    else:
        raise ValueError
    playlist_content = parse_string_playlist(request.form["playlist-content"])
    added_tracks, missed_tracks = create_playlist_through_flask_app(
        playlist_name, playlist_content, session.get("OAUTH_TOKEN"), playlist_description
    )
    return render_template(
        "submit.html",
        playlist_name=playlist_name,
        playlist_description=playlist_description,
        added_tracks=added_tracks,
        missed_tracks=missed_tracks,
        delimiter=delimiter,
    )


def create_playlist_through_flask_app(playlist_display_name, playlist_tracks, user_oauth_token, playlist_description):
    playlist = Playlist(playlist_display_name, playlist_tracks)
    if not playlist.spotify_init(user_oauth_token, playlist_description):
        raise PlaylistNotInitializedError
    return playlist.spotify_add_tracks(user_oauth_token)


@app.errorhandler(PlaylistNotInitializedError)
def handle_bad_request(e):
    return "Playlist was not properly initialized", 400


@app.errorhandler(UnsuccessfulGetRequest)
def handle_bad_request(e):
    return "Invalid GET request was processed. This is likely an error with the app itself or the playlist input.", 400
