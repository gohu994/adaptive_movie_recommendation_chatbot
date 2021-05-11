import pandas as pd

class Film:
    def __init__(self,id,title, year='', age='', imdb='', rotten='', netflix=0, \
    hulu=0, prime=0, disney=0, directors='', genre='', country='', language='', runtime=''):
        self.ID = id
        self.title = title
        self.year = year
        self.age = age
        self.imdb = imdb
        self.rotten = rotten
        self.netflix = netflix
        self.hulu = hulu
        self.prime = prime
        self.disney = disney
        self.directors = directors
        self.genre = genre
        self.country = country
        self.language = language
        self.runtime = runtime
    
    def getID(self,titre):
        return self.ID

    def getYear(self):
        return self.year

    def getDirectors(self):
        dir = self.directors.split(',')
        list_dir = [d for d in dir]
        return list_dir

    def getGenres(self):
        gen = self.genres.split(',')
        list_gen = [g for g in gen]
        return list_gen

    def getCountry(self):
        cou = self.country.split(',')
        list_cou = [c for c in cou]
        return list_cou

    def getLanguage(self):
        lan = self.language.split(',')
        list_lan = [l for l in lan]
        return list_lan

    def makeRow(self,data):
        newRow = [pd.Series([self.ID,self.title,self.year,self.age,self.imdb,self.rotten,self.netflix,self.hulu,self.prime,\
            self.disney,self.directors,self.genre,self.country,self.language,self.runtime],index=data.columns)]
        return newRow