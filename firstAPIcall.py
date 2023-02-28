import tmdbsimple as tmdb

# set up API key
tmdb.API_KEY = '3acd4a216c74c749376f9d840b43977c'

# search for movies with keyword 'Batman'
search = tmdb.Search()
response = search.movie(query='Batman')

# print the results
for result in search.results:
    print(result['title'])