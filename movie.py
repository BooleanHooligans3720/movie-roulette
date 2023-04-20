import tmdbsimple as tmdb

#basic class to store info about the movie
class movie:

  def __init__(self, id):
    self.id = id

    #one call to the API and stores the data
    self.info = tmdb.Movies(self.id).info()
    #assigns data to the variables
    self.title = self.info['title']
    self.genre = self.info['genres'][0]['name']
    self.runtime = int(self.info['runtime'])
    self.popularity = self.info['popularity']
    self.date = int(self.info['release_date'][0:4])
    #self.printInfo()

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

    #function to print the data
  def printInfo(self):
    print("Title: ", self.title, "\nID: ", self.id, "\nGenre: ", self.genre, "\nRuntime: ",
          self.runtime, "\nPopularity: ", self.popularity, "\nRelease date: ",
          self.date)
    return
