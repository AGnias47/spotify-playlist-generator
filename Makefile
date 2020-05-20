#
#   A. Gnias
#
#   Makefile - Used for SpotifyAPI Repository
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Make 4.2.1
#   Vim 8.0

PYTHON = python3
VIEWER = less
README_VIEWER = mdless
SHELL = bash

.PHONY : clean view readme license runnode apidocs \
utest_Playlist utest_Track test utest_Artist utest_Album utest \
ftest_Playlist ftest_Track ftest_general test_parameterinput ftest \
test run

clean :
	git clean -dxf -e keys.json -e .idea/

view : playlist_generator.py
	$(VIEWER) playlist_generator.py

readme : README.md
	${README_VIEWER} README.md

license : LICENSE
	$(VIEWER) LICENSE

runnode : 
	node ~/spotify_auth_page/app.js

refresh :
	$(PYTHON)  ./spotify_token_refresh/refresh.py

apidocs :
	cd sphinx && sphinx-apidoc -f -o source/ ../.

test :
	rm -rf auth_page/node_modules/ && pytest


run : playlist_generator.py
	$(PYTHON) playlist_generator.py -k keys.json -f playlist.csv -n Spotify_API_$$(date +%m_%d_%Y) -d "Playlist from the spotify API"


