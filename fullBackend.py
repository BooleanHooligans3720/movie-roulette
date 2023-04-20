import tmdbsimple as tmdb
import requests
import json
import randomPicker
import movie
from typing import List

# set up API keys
tmdb.API_KEY = '3acd4a216c74c749376f9d840b43977c'
headers = {
	"X-RapidAPI-Key": "4a7b7c4310mshb50633bd3c4859ap1a7745jsn43373ef85cb8",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}
url = "https://streaming-availability.p.rapidapi.com/v2/get/basic"

# search for movies with a specified keyword
search = tmdb.Search()

# PLACEHOLDER for UI search
print("Please enter a keyword to search for:")
title = input()

response = search.movie(query=title)

# PLACEHOLDER 
# show the first 15 results of the search using the slicing method [:#:]
for result in search.results[:15:]:
	if (len(result['title']) > 48):
		print((result['title'][0:45] + "...").ljust(50, ' '), "Movie ID:", result['id'])
	else:
		print(result['title'].ljust(50, ' '), "Movie ID:", result['id'])

idList = []

#PLACEHOLDER
# get list of movie ids
# right now I'm doing it by typing in movie IDs, but if you find a way to change that go ahead
another = 'y'
while (another == 'y' or another == 'Y'):
    
	print("\nPlease enter a movie ID to add to the list:")
 
	movieID = input()
 
	idList.append(movieID)
	
	print("Do you want to add another movie to the list?\nPlease enter y or n:")
	another = input()
 
	while (another != 'y' and another != 'Y' and another != 'n' and another != 'N'):
		print("Please enter y or n:")
		another = input()

# PLACEHOLDER - this doesn't necessarily need to be shown in the UI, up to y'all
# print list of movies in list
print("\nMovies in list:")
for i in idList:
	title = tmdb.Movies(i).info()['title']
	if (len(title) > 48):
		print(title[0:45] + "...")
	else:
		print(title)
  
movieList: List[movie.movie] = []

# Populate the list of movie objects: 
for i in idList:
    #call movie constructor on each ID to populate
    newMovie = movie.movie(i)
    movieList.append(newMovie)
      
# integrate list into the randomizer to get back a single movie object
movieResult = randomPicker.getWeightedRandom(movieList)

# PLACEHOLDER 
# print movie info
print("RESULT:\n")
movieResult.printInfo()

# MOVING ON TO STREAMING AVAILABILITY API

# for tmdb_id, must preface the number with 'movie/'
queryString = {"country":"us","tmdb_id":"movie/" + str(movieResult.getID()) }

# Streaming Avail. API request
response = requests.request("GET", url, headers=headers, params=queryString)

# text string of json data returned from Streaming Avail API
data = json.loads(response.text)

# ALL PRINT STATEMENTS ARE PLACEHOLDERS
# probably need to change these to global booleans or something to pass to UI
if ('apple' in data['result']['streamingInfo']['us']):
    print("Available on Apple")
            
if ('Netflix' in data['result']['streamingInfo']['us']):
    print("Available on Netflix")
    
if ('prime' in data['result']['streamingInfo']['us']):
    print("Available on Amazon Prime")
    
if ('Disney' in data['result']['streamingInfo']['us']):
    print("Available on Disney+")
    
if ('hbo' in data['result']['streamingInfo']['us']):
    print("Available on HBO Max")
    
if ('hulu' in data['result']['streamingInfo']['us']):
    print("Available on Hulu")
    
if ('peacock' in data['result']['streamingInfo']['us']):
    print("Available on Peacock")
    
if ('paramount' in data['result']['streamingInfo']['us']):
    print("Available on Paramount")
    
if ('starz' in data['result']['streamingInfo']['us']):
    print("Available on Starz")
    
if ('showtime' in data['result']['streamingInfo']['us']):
    print("Available on Showtime")
    
if ('mubi' in data['result']['streamingInfo']['us']):
    print("Available on Mubi")
