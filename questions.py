import database
import personality
import re
import recommend

def ask_Netflix(texto,nombre,id):
    answer = 'Now that I know more about your personality, I have to ask you few technical questions more concerning the streaming platforms you have.\n\nDo you have access to Netflix ?'
    return answer

def ask_Hulu(texto,nombre,id):
    netflix = 0
    if re.search('yes', texto, re.IGNORECASE)!=None:
        netflix = 1
    answer = 'Do you have Hulu?'
    return answer,netflix

def ask_Prime(texto,nombre,id):
    hulu = 0
    if re.search('yes', texto, re.IGNORECASE)!=None:
        hulu = 1
    answer = 'Do you have Prime Video?'
    return answer,hulu

def ask_Disney(texto,nombre,id):
    prime = 0
    if re.search('yes', texto, re.IGNORECASE)!=None:
        prime = 1
    answer = 'Do you have DisneyPlus?'
    return answer,prime

def performing(texto,nombre,id):
    disney = 0
    if re.search('yes', texto, re.IGNORECASE)!=None:
        disney = 1
    answer = 'Saving responses, please hang on a second...\nPlease write \'Ok\' when ready to continue the experience.'
    return answer,disney

def platforms_saved(texto,nombre,id,plat):
    database.updateUser(id,nombre,'platforms',plat)
    answer = "Which is, according to you, the best duration of a movie ? (in minutes)"
    return answer
    
def ask_recentness(texto,nombre,id):
    best_duration = int(texto)
    database.updateUser(id,nombre,'duration',best_duration)
    answer = "Ok, do you want to watch a recent, intermediate or old movie ?"
    return answer
    
def ask_other(texto,nombre,id):
    year = 0
    if re.search('old', texto, re.IGNORECASE)!=None:
        year = 1985
    elif re.search('recent', texto, re.IGNORECASE)!=None:
        year = 2010
    database.updateUser(id,nombre,'fav_year',year)
    answer = "How many movies do you want me to suggest ?"
    return answer
    
def ask_n_best(texto,nombre,id):
    nb = re.findall('[0-9]+', texto)[0]
    answer = "Thank you very much for all the information! I am now looking for some movies you will love.\nType 'Go' to get the results."
    return answer,nb