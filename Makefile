PYTHON = python3
VIEWER = less
README_VIEWER = mdless
SHELL = bash
BROWSER = google-chrome
COVERAGE = coverage
TEST_MODULE = pytest

.PHONY : clean view readme static license run_authpage refresh test search run docs sview format

help:                                                  ## Show this help message
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

clean :                                                ## Clean the repo
	git clean -dxf -e keys.json -e .idea/ -e .vscode/

readme : README.md                                     ## View the ReadMe
	$(README_VIEWER) README.md

license : LICENSE                                      ## View the license
	$(VIEWER) LICENSE

run_authpage :                                         ## Run the GUI for auth credentials
	node auth_page/app.js

refresh :                                              ## Refresh an existing token
	$(PYTHON)  ./spotifytools/token_refresh.py

static:                                                ## Linting
	pylint --disable=C0103,C0301,R1711,R1705,R0903,R1734,W1514 spotifytools/ || true

test :                                                 ## Run unit tests
	rm -rf auth_page/node_modules/ && $(COVERAGE) run -m $(TEST_MODULE) -s && $(COVERAGE) report && coverage-badge

search : track_searcher.py                             ## Search for a track
	$(PYTHON) track_searcher.py

run : playlist_generator.py                            ## Generate a playlist
	$(PYTHON) playlist_generator.py -k keys.json -f playlist.csv -n Spotify_API_$$(date +%m_%d_%Y) -d "Playlist from the spotify API"

format :                                               ## Format using black
	black -l 120 .

docs : sphinx/update_documentation.bash                ## Generate Sphinx documentation
	cd sphinx && bash update_documentation.bash

sview : docs/index.html                                ## View Sphinx documentation
	$(BROWSER) docs/index.html
