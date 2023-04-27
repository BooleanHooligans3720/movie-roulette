import tmdbsimple as tmdb
import requests
import json
import randomPicker
import movie
from typing import List

# set up API keys
tmdb.API_KEY = ''
headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}
url = "https://streaming-availability.p.rapidapi.com/v2/get/basic"


class Backend:
    
	def __init__(self):
		self.movieList: List[movie.movie] = []
		self.netflix = False
		self.apple = False
		self.prime = False
		self.disney = False
		self.hbo = False
		self.hulu = False
		self.peacock = False
		self.paramount = False
		self.starz = False
		self.showtime = False
		self.mubi = False

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
	
	# give a movie ID to add to the list of movies to pick from
	def addToList(self, movieID):
		movieToAdd = movie.movie(movieID)
		self.movieList.append(movieToAdd)
		return
     
    # only called in movieRouletteSpin()
	def setStreamingServices(self, movieID):
		# for tmdb_id, must preface the number with 'movie/'
		queryString = {"country":"us","tmdb_id":"movie/" + str(movieID) }

		# Streaming Avail. API request
		response = requests.request("GET", url, headers=headers, params=queryString)

		# text string of json data returned from Streaming Avail API
		data = json.loads(response.text)

		# set all booleans
		if ('apple' in data['result']['streamingInfo']['us']):
			self.apple = True
					
		if ('Netflix' in data['result']['streamingInfo']['us']):
			self.netflix = True
			
		if ('prime' in data['result']['streamingInfo']['us']):
			self.prime = True
   
		if ('Disney' in data['result']['streamingInfo']['us']):
			self.disney = True
			
		if ('hbo' in data['result']['streamingInfo']['us']):
			self.hbo = True
			
		if ('hulu' in data['result']['streamingInfo']['us']):
			self.hulu = True
			
		if ('peacock' in data['result']['streamingInfo']['us']):
			self.peacock = True
			
		if ('paramount' in data['result']['streamingInfo']['us']):
			self.paramount = True
			
		if ('starz' in data['result']['streamingInfo']['us']):
			self.starz = True
			
		if ('showtime' in data['result']['streamingInfo']['us']):
			self.showtime = True
			
		if ('mubi' in data['result']['streamingInfo']['us']):
			self.mubi = True

		return
         
	def getList(self):
		return self.movieList

	# right now we can only spin once before the program has to be reloaded 
	def movieRouletteSpin(self):
		result: movie.movie = randomPicker.getWeightedRandom(self.movieList)

		# reset streaming availability to make a clean slate for the next movie called
		self.netflix = False
		self.apple = False
		self.prime = False
		self.disney = False
		self.hbo = False
		self.hulu = False
		self.peacock = False
		self.paramount = False
		self.starz = False
		self.showtime = False
		self.mubi = False
	
		# update streaming availability for current movie
		self.setStreamingServices(result.getID())
  
		return result

	def getNetflix(self):
		return self.netflix

	def getApple(self):
		return self.apple

	def getPrime(self):
		return self.prime

	def getDisney(self):
		return self.disney

	def getHBO(self):
		return self.hbo

	def getHulu(self):
		return self.hulu

	def getPeacock(self):
		return self.peacock

	def getParamount(self):
		return self.paramount

	def getStarz(self):
		return self.starz

	def getShowtime(self):
		return self.showtime

	def getMubi(self):
		return self.mubi
