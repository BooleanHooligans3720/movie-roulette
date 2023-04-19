import tmdbsimple as tmdb
import movie 
import randomPicker

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

#list that holds the movies as objects 
listOBJ = []
#converts the list of IDs into a list of movie objects
for x in idList:
  holder = movie.movie(x)
  listOBJ.append(holder)

#outputs the chosen movie
print (randomPicker.randomPicker(listOBJ))