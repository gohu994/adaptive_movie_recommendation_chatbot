import json
import pandas as pd
import csv
import re

import database

def restrict_personality(id,name):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))

    gen = us['genres']
    before = database.data
    
    g = gen.split(',')
    subsetDataFrame = before[before.Genres.str.contains('|'.join(g))]

    return subsetDataFrame

def restrict_languages(id,name):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))

    gen = us['language']
    before = restrict_personality(id,name)
    
    g = gen.split(',')
    subsetDataFrame = before[before.Language.str.contains('|'.join(g))]

    return subsetDataFrame

def restrict_age(id,name):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))

    g = us['age']
    before = restrict_languages(id,name)
    subsetDataFrame = before[pd.to_numeric(before['Age'].astype(int)) <= g]
    return subsetDataFrame

def restrict_platform(id,name):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))

    g = us['platforms']
    before = restrict_age(id,name)
    if g != [0,0,0,0]:
        subsetDataFrame = before[((pd.to_numeric(before['Netflix'].astype(int)) == g[0]) & g[0]==1) | ((pd.to_numeric(before['Hulu'].astype(int)) == g[1]) & g[1]==1) | ((pd.to_numeric(before['Prime Video'].astype(int)) == g[2]) & g[2]==1) | ((pd.to_numeric(before['Disney+'].astype(int)) == g[3]) & g[3]==1)]
        return subsetDataFrame
    else:
        return before

def restrict_duration(id,name):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))

    g = us['duration']
    before = restrict_platform(id,name)
    if g != 0:
        subsetDataFrame = before[(pd.to_numeric(before['Runtime'].astype(int)) <= (1.1*g)) & (pd.to_numeric(before['Runtime'].astype(int)) >= (0.9*g))]
        return subsetDataFrame
    else:
        return before


def restrict_recentness(id,name):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))

    g = us['fav_year']
    before = restrict_duration(id,name)
    if g == 1985:
        subsetDataFrame = before[(pd.to_numeric(before['Year'].astype(int)) <= g)]
        return subsetDataFrame
    elif g == 2010:
        subsetDataFrame = before[(pd.to_numeric(before['Year'].astype(int)) >= g)]
        return subsetDataFrame
    return before

def restrict_feedback(id,name):
    with open('users/'+str(id)+'_'+name+'/'+str(id)+'_'+name+'.json','r') as js:
        us = eval(json.load(js))

    di = us['directors']
    coun = us['fav_countries']

    before = restrict_recentness(id,name)

    if di != '':
        di = di.split(',')
        before.loc[before.Directors.str.contains('|'.join(di)), 'IMDb'] = pd.to_numeric(before.IMDb)+1
        before.loc[before.Directors.str.contains('|'.join(di)), 'Rotten Tomatoes'] = pd.to_numeric(before['Rotten Tomatoes'])+5
    if coun != '':
        coun = coun.split(',')
        before.loc[before.Country.str.contains('|'.join(coun)), 'IMDb'] = pd.to_numeric(before.IMDb)+1
        before.loc[before.Country.str.contains('|'.join(coun)), 'Rotten Tomatoes'] = pd.to_numeric(before['Rotten Tomatoes'])+5
    new = before[~before['ID'].isin(us['seen'])]
    return new


def take_n_best(texto,nombre,id,n):
    before = restrict_feedback(id,nombre)
    before['Rotten Tomatoes'] = pd.to_numeric(before['Rotten Tomatoes'])
    before_sorted = before.sort_values(by=['Rotten Tomatoes'],ascending=False)
    n_best = before_sorted.head(int(n))
    recom = n_best.to_csv(header=None, index=False).strip('\n').split('\n')
    answer = "Here are the movies I suggest you:\n\n"
    database.save_recom(id,nombre,recom)
    for r in recom:
        rec = r.split(',')
        platforms = ['Netflix', 'Hulu', 'Prime Video', 'Disney\+']
        pl = ""
        for i in range(6,10):
            if int(rec[i]) != 0:
                pl += platforms[i-6] + ', '
        if pl != "":
            answer += '- ' + str(rec[1]) + '\t(' + str(rec[2]) + ') on ' + pl[0:-2] + '\n'
        else:
            answer += '- ' + str(rec[1]) + '\t(' + str(rec[2]) + ')\n'
    answer += '\n\nIf you want to launch again the experience, please type \'restart\', if not, type \'bye\'.'
    return recom,answer


def ask_seen(texto,name,id):
    answer = 'So, what did you think of the movies we talked about last time ? You have below the list of them, please type the numbers of those you HAVE SEEN.\n'
    answer += '\n(Type 0 if none)\n'
    r = []
    with open('users/'+str(id)+'_'+name+'/'+'recommendations.csv','r') as reco:
        csv_reader = csv.reader(reco)
        for row in csv_reader:
            r.append(row)
    for i in range(len(r)):
        answer += '\n%d: %s' % (i+1,r[i][1])
    return answer

def ask_liked(texto,name,id):
    answer = 'Among these films, which are those you LIKED?\n'
    seen = re.findall('[0-9]+', texto)
    r = []
    seen_ids = []
    with open('users/'+str(id)+'_'+name+'/'+'recommendations.csv','r') as reco:
        csv_reader = csv.reader(reco)
        for row in csv_reader:
            r.append(row)
    for i in seen:
        i = int(i)
        if i != 0:
            seen_ids.append(int(r[i-1][0]))
    database.updateUser(id,name,'seen',seen_ids)
    return answer

def ask_disliked(texto,name,id):
    answer = 'Now, which one did you DISLIKE?\n'
    liked = re.findall('[0-9]+', texto)
    r = []
    liked_ids = []
    dirs = '' #10
    countries = '' #12
    with open('users/'+str(id)+'_'+name+'/'+'recommendations.csv','r') as reco:
        csv_reader = csv.reader(reco)
        for row in csv_reader:
            r.append(row)
    for i in liked:
        i = int(i)
        if i!=0:
            liked_ids.append(int(r[i-1][0]))
            dirs += r[i-1][10]
            countries += r[i-1][12]
    database.updateUser(id,name,'liked',liked_ids)
    database.updateUser(id,name,'directors',dirs)
    database.updateUser(id,name,'fav_countries',countries)
    return answer

def process_feedback(texto,name,id):
    answer = 'Processing...\n'
    disliked = re.findall('[0-9]+', texto)
    r = []
    disliked_ids = []
    with open('users/'+str(id)+'_'+name+'/'+'recommendations.csv','r') as reco:
        csv_reader = csv.reader(reco)
        for row in csv_reader:
            r.append(row)
    for i in disliked:
        i = int(i)
        if i != 0:
            disliked_ids.append(int(r[i-1][0]))
    database.updateUser(id,name,'unliked',disliked_ids)
    

    answer += 'Please type \'Ok\' to go on.'
    return answer