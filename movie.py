import tmdbsimple as tmdb

#basic class to store info about the movie
class movie:

  def __init__(self, id):
    self.id = id

    #one call to the API and stores the data
    self.info = tmdb.Movies(self.id).info()
    #assigns data to the variables
    self.title = self.info['title']
    if(self.info['genres']):
      self.genre = self.info['genres'][0]['name']
    else:
          self.genre = None
    if(self.info['runtime']):
      self.runtime = int(self.info['runtime'])
    else:
          self.runtime = None
    if(self.info['popularity']):
      self.popularity = self.info['popularity']
    else:
          self.popularity = None
    if(self.info['release_date']):
          self.date = int(self.info['release_date'][0:4])
    else:
          self.date = None
    #self.printInfo()
    if(self.info['overview']):
      self.description = (self.info['overview'])
    else:
          self.description = None
    if(self.info['poster_path']):
       self.poster_path = self.info['poster_path']
       print(self.poster_path)
    else:
       self.poster_path = None

  def getID(self):
    return self.id

  #basic getter functions
  def getTitle(self):
    return self.title

  def getGenre(self):    
    return self.genre

  def getRuntime(self):
    return self.runtime

  def getPopularity(self):
    return self.popularity

  def getDate(self):
      return self.date
  
  def getDescription(self):
    return self.description
  def getPoster(self):
     return self.poster_path

    #function to print the data
  def printInfo(self):
    print("Title: ", self.title, "\nID: ", self.id, "\nGenre: ", self.genre, "\nRuntime: ",
          self.runtime, "\nPopularity: ", self.popularity, "\nRelease date: ",
          self.date)
    return
