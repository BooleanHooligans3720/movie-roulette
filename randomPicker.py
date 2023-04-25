import random
import movie
from typing import List
import tmdbsimple as tmdb



def getWeightedRandom(movieList: List[movie.movie],genre,runtimeMin,runtimeMax,popularity,dateMin,dateMax):
    
  # booleans to determine if the user wants to weight the search on these options 
	genreChoice = False
	runtimeChoice = False
	minimumPopularityChoice = False
	releaseDecadeChoice = False
	#check for filters being used

  # some movies have multiple genres but the json parsing works best with just the first 
	# Here are the list of genres and their corresponding codes: 
		# MOVIE			 ####
		# Action          28
		# Adventure       12
		# Animation       16
		# Comedy          35
		# Crime           80
		# Documentary     99
		# Drama           18
		# Family          10751
		# Fantasy         14
		# History         36
		# Horror          27
		# Music           10402
		# Mystery         9648
		# Romance         10749
		# Science Fiction 878
		# TV Movie        10770
		# Thriller        53
		# War             10752
		# Western         37
	if (genre != ""):
		genreChoice = True
    
  # should be a dropdown for range (ex 100-120 min, 120-150 min, etc.)
	if (runtimeMin != "" or runtimeMax != ""):
		runtimeChoice = True

  # should be a minimum value (ex >= 35 popularity) (popularity is a score /100 as far as I can tell)
	if (popularity != ""):
		minimumPopularityChoice = True

  # should be a range (ex 1980-1989)
	if (dateMin != "" or dateMax != ""):
		releaseDecadeChoice = True
    
  #no params and the movie list is empty, will create and return a movie obj with a random ID
	if not genreChoice and not runtimeChoice and not minimumPopularityChoice and not releaseDecadeChoice and len(movieList) == 0:
		return getRandomID()
    
    # no params selected, get pure random from the list
	if not genreChoice and not runtimeChoice and not minimumPopularityChoice and not releaseDecadeChoice:
		return getPureRandom(movieList)

	# couldn't figure out how to do weighted random based on an unknown amount of filters so I'm doing it this way
	newMovieList: List[movie.movie] = []
 
	# PLACEHOLDER- needs to match the 
	# New list of movies that meet the criteria given. If a movie meets more than 1 criteria 
 	# it's on the list multiple times to make it more likely to be picked
	for x in movieList:
		if (x.getGenre == genre):
			newMovieList.append(x)
   
		if (x.getRuntime >= str(runtimeMin) and x.getRuntime < str(runtimeMax)):
			newMovieList.append(x)
   
		if (x.getPopularity >= str(popularity)):
			newMovieList.append(x)
   
		if (x.getDate >= str(dateMin) and x.getDate < str(dateMax)):
			newMovieList.append(x)
	
	# check to make sure there's movies in newMovieList
	# UP TO UI GUYS- either throw an error or just leave it like this to pick a purely random movie 

  
	if (newMovieList.count() == 0):
		return getPureRandom(movieList)
   
	return random.choice(newMovieList)

# used whenever no parameters are selected (all booleans false)
def getPureRandom(movieList: List[movie.movie]):
	return random.choice(movieList)

#if the list of movies and the params are all blank this will return a random movie
def getRandomID():
	temp: movie.movie
	while (True):
		try:
			temp = movie.movie(random.randint(1, 9999))
			return temp
		except:
			print()
	return temp

# random.randint(1, 9999)
