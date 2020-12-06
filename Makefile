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
BROWSER = google-chrome
COVERAGE = coverage
TEST_MODULE = pytest

.PHONY : clean view readme license run_authpage refresh test search run docs sview format

clean :
	git clean -dxf -e keys.json -e .idea/

readme : README.md
	$(README_VIEWER) README.md

license : LICENSE
	$(VIEWER) LICENSE

run_authpage :
	node auth_page/app.js

refresh :
	$(PYTHON)  ./spotify_token_refresh/refresh.py

test :
	rm -rf auth_page/node_modules/ && $(COVERAGE) run -m $(TEST_MODULE) -s && $(COVERAGE) report && coverage-badge

search : track_searcher.py
	$(PYTHON) track_searcher.py

run : playlist_generator.py
	$(PYTHON) playlist_generator.py -k keys.json -f playlist.csv -n Spotify_API_$$(date +%m_%d_%Y) -d "Playlist from the spotify API"

format :
	black -l 120 .

docs : sphinx/update_documentation.bash
	cd sphinx && bash update_documentation.bash

sview : docs/index.html
	$(BROWSER) docs/index.html
