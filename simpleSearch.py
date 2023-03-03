import tmdbsimple as tmdb

# set up API key
tmdb.API_KEY = '3acd4a216c74c749376f9d840b43977c'

# search for movies with a specified keyword
search = tmdb.Search()

print("Please enter a keyword to search for:")

title = input()

response = search.movie(query=title)

# print the results
for result in search.results:
    print(result['title'].ljust(60, ' '), "Movie ID:", result['id'])
    
