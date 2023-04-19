import random
import movie

def randomPicker(list):

  #this is a placeholder
  # remove when implemented
  print("answer a few questions, if no preference juts hit enter!\n")
  genre = input("what genre do you want?\n")
  actors = input("what actors do you want to see? \n")
  
  runtime = input("how long to you want the movie?\n")
  
  popularity = input("how popular do you want the movie?\n")
  
  date = input("what decades do you want the movie to be from?\n")

  ###
  ###
  sizeArray = []
  randomSize = 0
  #if/else statements for checking if each aspect of the movie for the index matches the requirements, ie actor, genre etc.
  for x in list:
    total = 1
  
    if (x.getGenre == genre):
      total + 5
      
    if (x.getActors == actors):
      total +=5
      
      #length is the same
    if ((int(x.getRuntime()) % 15) * 15 == runtime):
      total+=7
      print("here ->>" + x.getRuntime)
    elif((int(x.getRuntime()) % 15) * 15 + 15 > x.getRuntime() or (int(x.getRuntime()) % 15) * 15 - 15 < int(runtime)):
      total+=5
      
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

#prints chosen movie    
  for x in sizeArray:
    if (x >= randVal):
      print(x)