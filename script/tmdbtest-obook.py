import json
import sys
import os
import requests as req

import tmdbsimple as tmdb

def main():
    if len(sys.argv) <= 2:
        print(f"usage: {sys.argv[0]} MOVIE_TITLE", file=sys.stderr)

    with open("../tmdbKEY") as keyFile:
        tmdb.API_KEY = keyFile.read()

    searchTitle = sys.argv[1]

    search = tmdb.Search()
    response = search.movie(query=searchTitle)
    print(response)

    for t in search.results:
        print(s)


if __name__ == '__main__':
    main()