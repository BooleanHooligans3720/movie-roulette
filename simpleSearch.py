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
	if (len(result['title']) > 48):
		print((result['title'][0:45] + "...").ljust(50, ' '), "Movie ID:", result['id'])
	else:
		print(result['title'].ljust(50, ' '), "Movie ID:", result['id'])
    
another = 'y'

idList = []

# get list of movie ids
while (another == 'y' or another == 'Y'):
	print("\nPlease enter a movie ID to add to the list:")
	movieID = input()
 
	idList.append(movieID)
	
	print("Do you want to add another movie to the list?\nPlease enter y or n:")
	another = input()
 
	while (another != 'y' and another != 'Y' and another != 'n' and another != 'N'):
		print("Please enter y or n:")
		another = input()

# print list of movies selected
print("\nMovies in list:")
for i in idList:
	title = tmdb.Movies(i).info()['title']
	if (len(title) > 48):
		print(title[0:45] + "...")
	else:
		print(title)