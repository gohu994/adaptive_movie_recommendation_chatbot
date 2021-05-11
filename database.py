import pandas as pd
import numpy as np
import csv
from datetime import datetime
import os

from Film import Film
from User import User

data = pd.read_csv('movies.csv',usecols=['ID', 'Title', 'Year', 'Age', 'IMDb', 'Rotten Tomatoes',
       'Netflix', 'Hulu', 'Prime Video', 'Disney+', 'Directors',
       'Genres', 'Country', 'Language', 'Runtime'])

data['Age'].fillna(value=0, inplace=True)
data['IMDb'].fillna(value=0, inplace=True)
data['Rotten Tomatoes'].fillna(value=0, inplace=True)
data['Runtime'].fillna(value=0, inplace=True)
data.fillna(value='', inplace=True)

def addMovie(title, year='', age='', imdb='', rotten='', netflix=0, \
    hulu=0, prime=0, disney=0, directors='', genre='', country='', language='', runtime=''):
    
    newID = data.tail(1).iloc[0]['ID']+1
    f = Film(newID,title, year, age, imdb, rotten, netflix,hulu, prime, disney, directors, genre, country, language, runtime)
    newRow = f.makeRow(data)
    
    da = data.append(newRow)
    da.to_csv('movies.csv')
    return da

def listGenres():
    distinct_genres = []
    for lines in data['Genres']:
        g = lines.split(',')
        for elt in g:
            if elt not in distinct_genres and elt != '':
                distinct_genres.append(elt)
    return distinct_genres

list_genres = listGenres()

import json
def newUser(Id,name,age,country,language):
    # context: user not already known
    new_user = User(Id,name,age,country,language)
    json_usr = json.dumps(new_user.toDict())
    os.mkdir('users/'+str(Id)+'_'+name)
    with open('users/'+str(Id)+'_'+name+'/'+str(Id)+'_'+name+'.json','w') as json_file:
        json.dump(json_usr,json_file,indent=4, sort_keys=True)
    lista_users = pd.read_csv('users/users.csv',usecols=['ID','Name'])
    newRow = [pd.Series([Id,name],index=['ID','Name'])]
    lista_users.append(newRow).to_csv('users/users.csv')
    return 0

def isKnown(id,name):
    lista_users = pd.read_csv("users/users.csv",usecols=['ID','Name'])
    if id not in lista_users['ID'].tolist():
        return False
    else:
        return True

def updateUser(id,name,attribute,value):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))
    new_us = us
    if attribute == 'liked' or attribute == 'unliked' or attribute == 'seen':
        temp = us[attribute]
        print('temp',temp)
        for elt in value:
            temp.append(elt)
        new_us[attribute] = temp
    
    elif (attribute == 'directors' or attribute == 'countries') and type(value)==str:
        new_us[attribute] += ','+value
    
    else:
        new_us[attribute] = value
    
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','w') as modified:
        json.dump(str(new_us),modified,indent=4)

    return 0

def save_recom(id,name,recom):
    # input: list of rows recommendations
    with open('users/'+str(id)+'_'+name+'/'+'recommendations.csv','w+') as reco:
        line = ''
        for r in recom:
            line = r + '\n'
            reco.write(line)
    return 0


#updateUser(1690350938,'Hugo','personality',[0,1,2,3,4])
#updateUser(1690350938,'Hugo','genres',['Action,War,Comedy'])

#newUser(0,'hbena',22,'France','French')
#resp = isKnown(1,'hena')
#updateUser(1690350938,'Hugo','personality',[20, 35, 34, 16, 39])
