# Spotify Playlist Generator

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description

This project allows a user to create a Spotify playlist from a csv file of the form

```csv
Artist, Song
```

This is done by utilizing the Spotify API detailed [on the Spotify developer
website](https://developer.spotify.com/documentation/web-api/).

This project also contains an authorization app for generating an initial access and refresh token. This app was pulled
 from the `authorization_code` directory within
 [spotify/web-api-auth-examples](https://github.com/spotify/web-api-auth-examples). The License for that project is
 included in the `auth_page` repo.

## Source Code
Link: https://github.com/AGnias47/SpotifyAPI

## Requirements

### System Requirements

* python >= 3.7
* pip
* node
* npm

### Spotify Playlist Generator PyPi Dependencies

```requirements.txt
requests==2.23.0
fuzzywuzzy==0.17.0
```

### Auth Page npm Dependencies

```json
  "dependencies": {
    "cookie-parser": "1.3.2",
    "cors": "^2.8.4",
    "express": "~4.16.0",
    "npm": "^6.9.0",
    "querystring": "~0.2.0",
    "request": "~2.83.0"
  }
```

## Playlist Generation

### Creating a CSV Playlist

The playlist should be in a text file of the form

```csv
Artist, Song
```

If using a spreadsheet tool, such as Excel, add the artist to Column A and the song to Column B. Do not add column
 titles (ex. Row 1 should be the first song in your playlist). Ensure the file is saved as a CSV and not xlsx, etc.
 
The playlist uses fuzzy matching to determine which songs should be added. This makes the playlist generator forgiving
 of misspellings, missing commas, and incomplete titles of songs, among other things, but it does increase the likelihood
 of an unwanted song being added to your playlist. So it goes. The playlist generator currently uses a [Levenshtein
 distance](https://en.wikipedia.org/wiki/Levenshtein_distance) ratio of 0.75. This can be altered if too many / not
 enough songs from a playlist are being added.

### Initial Token Generation

Use of the playlist generator requires users to obtain their own `client_id` and `client_secret` token from the
 [Spotify Developer's Dashboard](https://developer.spotify.com/dashboard/applications). Once these tokens are obtained,
 follow the steps below to obtain your initial `access_token` and a `refresh_token`.

1. In the project root directory, create a `keys.json` file with the following contents:

    ```json
    {
        "client_id": "<Your Client ID>",
        "client_secret": "<Your Client Secret ID>",
        "access_token": "",
        "refresh_token": ""
    }
    ```
   
    The `access_token` and `refresh_token` are intentionally left blank for now, but should conform to valid JSON standards.
2. In the `auth_page` directory, run `npm install` to download the dependencies needed to run the auth page
3. In the project root directory, run `node ./auth_page/app.js`
4. Go to `localhost:8888` in a web browser and click "Log in with Spotify"
5. Authorize the app for access by logging in with your Spotify user credentials
6. Copy the `access_token` and `refresh_token` and use those values for the corresponding keys in the `keys.json` file

### Refreshing the Access Token

At this point, an access token has been generated, and the playlist generator is able to authenticate with Spotify.
 However, the access token expires after 1 hour. The access token can be regenerated using your refresh token via
 the following steps.
 
1. Ensure your `keys.json` file exists with all required fields. `client_id`, `client_secret`, and `refresh_token` must
 be accurate. If they are not, rerun the steps for "Initial Token Generation".
2. Run `./spotify_token_refresh/refresh.py`. The `access_token` in `keys.json` will be updated in place and should now
 be able to authenticate with Spotify.
 
The GUI method can always be used to generate a new access token, but this method allows for it to be updated directly
 from the command line.
 
### Running the Playlist Generator

Once the access token has been updated in `keys.json`, the playlist generator can be executed with the following command:

```bash
./playlist_generator.py -f <Path to csv playlist> -n <Playlist name> -d <Playlist description (Optional)>
```

The script will print to stdout which songs were and were not added to the playlist.


## Improvements

### Planned
 * Calculate coverage
    * Full coverage of existing classes and modules
 * Remove unnecessary code and classes
 * User testing with more diverse array of songs
 * Allow for usage of already created playlists
 * Add `black` icon
 * Documentation - repo description for directories, etc., instructions on other scripts, cases, technical descriptions
 * Update package structure
 
### Stretch

* GUI wrapper
* Update `auth_page` app
  * Remove unnecessary content
  * Rewrite in Flask
