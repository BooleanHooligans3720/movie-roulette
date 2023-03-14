import json
import sys
import os
import requests as req

import tmdbsimple as tmdb

def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} MOVIE_TITLE", file=sys.stderr)
        exit()

    with open("script\\tmdbKEY", mode='rt') as keyFile:
        tmdbKEY = keyFile.read()
        tmdb.API_KEY = tmdbKEY

    searchTitle = sys.argv[1]

    search = tmdb.Search()
    response = search.movie(query=searchTitle)
    #print(response)

    for t in search.results:
        print(t.keys())
        print(json.dumps(t, indent=4))

    print(response.keys())

    list_id = 143762 #random ass number i don't know how to find public lists
    listtest = req.get{'https://https://api.themoviedb.org/4/list/{list_id}', params={'page': '1', 'api_key': tmdbKEY}}


if __name__ == '__main__':
    main()