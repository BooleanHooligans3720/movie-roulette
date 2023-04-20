import random
import movie
from typing import List

def randomPicker(movieList: List[movie.movie]):

	#this is a placeholder
	# remove when implemented
	print("answer a few questions, if no preference juts hit enter!\n")
	genre = input("what genre do you want?\n")
	
	runtime = input("how long to you want the movie?\n")
	
	popularity = input("how popular do you want the movie?\n")
	
	date = input("what decades do you want the movie to be from?\n")

	###
	###
	sizeArray = []
	randomSize = 0
	#if/else statements for checking if each aspect of the movie for the index matches the requirements, ie actor, genre etc.
	for x in movieList:
		total = 1

		if (genre != ""):
			if (x.getGenre == genre):
				total + 5
		if (runtime != ""):
			#length is the same
			if ((int(x.getRuntime()) % 15) * 15 == runtime):
				total+=7
				print("here ->>" + x.getRuntime)
   
			elif((int(x.getRuntime()) % 15) * 15 + 15 > x.getRuntime() or (int(x.getRuntime()) % 15) * 15 - 15 < int(runtime)):
				total+=5
		if (popularity != ""):
			if (x.getPopularity() == popularity):
				total +=7
			
			elif(x.getPopularity() + 10 > int(popularity) or x.getPopularity() - 10 < int(popularity)):
				total+=5

		#increases max size of random
		randomSize += total
  
		#adds most recent value to list
		sizeArray.append(randomSize)
  
	#makes random value
	randVal = random.randint(1,randomSize)
	#selects movie based off of the weights

	#returns chosen movie 
	for x in sizeArray:
		if (x >= randVal):
			return x

def getWeightedRandom(movieList: List[movie.movie]):
    
    # booleans to determine if the user wants to weight the search on these options 
	genreChoice = False
	runtimeChoice = False
	minimumPopularityChoice = False
	releaseDecadeChoice = False
 
	# PLACEHOLDERS until line 98
 	# replace with UI inputs when implemented 
	# ALL OF THESE NEED TO BE DROP-DOWN MENUS so that we don't have to error check as much 
	print("\nanswer a few questions, if no preference just hit enter!\n")
 
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
	
	genre = input("what genre do you want?\n")
	
	# should be a dropdown for range (ex 100-120 min, 120-150 min, etc.)
	runtimeMin = input("input lower range for movie length in minutes\n")
	runtimeMax = input("input upper range for movie length in minutes\n")

	# should be a minimum value (ex >= 35 popularity) (popularity is a score /100 as far as I can tell)
	popularity = input("how popular do you want the movie?\n")
	
	# should be a range (ex 1980-1989)
	dateMin = input("what year do you want the movie to be released during after?\n")
	dateMax = input("what year do you want the movie to be released before?\n")
 
	# PLACEHOLDER check for filters being used
	if (genre != ""):
		genreChoice = True
  
	if (runtimeMin != "" or runtimeMax != ""):
		runtimeChoice = True
  
	if (popularity != ""):
		minimumPopularityChoice = True
  
	if (dateMin != "" or dateMax != ""):
		releaseDecadeChoice = True
	
    # no params selected, get pure random
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
