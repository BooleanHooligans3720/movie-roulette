import json

class Watchlist:
    # create from json (see GET /list/{list_id} in API v4)
    # no idea how to do this
    #def __init__(tmdblist):
        #self.movies = tmdblist.object_ids

    # create from list of integers representing movie ids
    # isn't this redundant?? am i stupid??
    def __init__(ids):
        self.list = ids

    # methods go here
    
