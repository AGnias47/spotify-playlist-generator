# SpotifyAPI
Development projects utilizing the Spotify API detailed at https://developer.spotify.com/documentation/web-api/

## End Goal
Create a method of creating a playlist from a csv of the form:
```
Artist, Song
```

## OAuth Token retrieval
Currently just getting this by running the steps listed at https://github.com/spotify/web-api-auth-examples.

There is probably an easier way to do this.

## Contents

### artist_module.py
Functions for querying information on a particular artist.

Running
```
./artist_module.py <OAUTH Token>
```
tests the module functionality by getting information on Seal from Spotify.

### general_functions.py
Functions needed that are not specific to the Spotify API

### Makefile
Test the artist module by saving your OAuth Token in a local file named 'OAuth_Token' and running:
```
make test
```

### playlist.csv
Sample data
