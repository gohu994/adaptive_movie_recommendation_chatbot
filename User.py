import pandas as pd

class User():
    
    def __init__(self,id,name,age,country,language):
        # basic details of the user
        self.id = id
        #self.alias = alias         # no need if use telegram id
        self.name = name
        self.age = age
        self.country = country
        self.language = language
        self.personality = []

        # interactions with film database
        self.liked = []
        self.unliked = []
        self.seen = []

        # changing parameters according to context
        self.platforms = [0,0,0,0]
        self.time = 0

        # Preferences to deduce from liked movies
        self.duration = 0
        #self.actores = []
        self.directors = ""
        self.genres = ""
        self.fav_year = 0
        self.fav_countries = ""
    
    def makeStringFromList(self,liste):
        obj = ''
        for elt in liste:
            obj = obj + elt + ','
        return obj[:-1]

    def makeRow(self):
        newRow = [pd.Series([self.id,self.name,self.age,self.country,self.language,self.makeStringFromList(self.liked),self.makeStringFromList(self.unliked),self.makeStringFromList(self.seen),\
            self.duration,self.directors,self.genres,self.fav_year,self.fav_countries],index=['ID','name','age','country',\
            'language','liked','unliked','seen','duration','directors','genres','fav_year','fav_countries'])]
        return newRow

    def toDict(self):
        me = {}
        me['id'] = self.id
        me['name'] = self.name
        me['age'] = self.age
        me['country'] = self.country
        me['language'] = self.language
        me['personality'] = self.personality
        me['liked'] = self.liked
        me['unliked'] = self.unliked
        me['seen'] = self.seen
        me['platforms'] = self.platforms
        me['time'] = self.time
        me['duration'] = self.duration
        me['directors'] = self.directors
        me['genres'] = self.genres
        me['fav_year'] = self.fav_year
        me['fav_countries'] = self.fav_countries
        return me
        