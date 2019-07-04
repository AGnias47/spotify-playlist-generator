#
#   A. Gnias
#
#   Makefile - Used for SpotifyAPI Repository
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Make 4.2.1
#   Vim 8.0 [tabstop=3]

PYTHON = python3
VIEWER = less
SHELL = bash

.PHONY : clean view license test run

clean :
	rm -rf *.pyc __pycache__

view : spotify_module.py
	$(VIEWER) spotify_module.py

license : LICENSE
	$(VIEWER) LICENSE

utest_Playlist : test/test_Playlist.py
	cd test && $(PYTHON) test_Playlist.py

utest_Track : test/test_Track.py
	cd test && $(PYTHON) test_Track.py

utest : utest_Playlist utest_Track

runnode : 
	node ~/spotifyapitestbed/web-api-auth-examples/authorization_code/app.js

ftest : test/test_spotify_module.py
	cd test && $(PYTHON) test_spotify_module.py $$(cat ../OAuth_Token)

run : spotify_module.py
	$(PYTHON) spotify_module.py $$(cat OAuth_Token)

