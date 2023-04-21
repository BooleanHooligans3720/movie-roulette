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

class Backend:
    
	def __init__(self):
		movieList: List[movie.movie] = []

	def searchMovies(searchQuery: str):
		# search for movies with a specified keyword
		search = tmdb.Search()

		# call api search function
		search.movie(query=searchQuery)
  
		searchList: List[movie.movie] = []

		# Populate the list of the first 15 movie objects:
		for i in search.results[:15:]:
			#call movie constructor on each ID to populate
			newMovie = movie.movie(i['id'])
			searchList.append(newMovie)
	
		return searchList
	
	#def addToList():
     
   # def getStreamingServices(movieID: int):
         
	#def getList():
	
	#def print():