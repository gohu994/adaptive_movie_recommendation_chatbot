import database

def greet(texto,nombre):
    answer = ''
    if '/start' in texto or 'hello!' in texto or 'hey!' in texto:
        answer += "Hi %s! I am HBot, your movie chatbot. How are you ?" % (nombre)
    elif 'bye' in texto:
        answer += "Hi %s! I am HBot, your movie chatbot. How are you ?" % (nombre)
        pass
    else:
        answer += "I beg your pardon? Type '/start' to begin the experience"
    return answer

def greet_answer(texto,nombre,id):
    answer = ''
    if 'you' in texto and '?' in texto:
        answer += 'I\'m good, thanks.\n'
    if 'ok' in texto or 'fine' in texto or 'good' in texto or 'well' in texto:
        answer += 'All right!'
    elif 'not' in texto or 'bad' in texto or 'sad' in texto or 'tired' in texto or 'sleepy' in texto:
        answer += 'Come here buddy, everything will be fine, just watch a movie, eat and sleep.'
    else:
        answer = 'Ok, let\'s begin'
    return answer

def begin_details_age(texto,nombre,id):
    answer = ''
    answer += '\nWe don\'t know each other yet!\nI am HBot, I am here to help you find good movies to watch.\nI\'m gonna ask you some questions, please answer by one or two words only.\nFor instance if I ask you about your age, your answer must contain only the digits of your age. If I ask about your country, answer should only be the name of the country.\nThank you very much, let\'s begin!\n\n'
    answer += 'How old are you, %s?' % (nombre)
    return answer

def ask_country(texto,nombre,id):
    # save age and ask country
    age = int(texto)
    answer = 'Where are you from ?'
    return age,answer

def ask_language(texto,nombre,id):
    # save country and ask language
    coun = texto
    answer = 'Which language(s) do you know ?\n(If several answers, please write like "A,B,C")'
    return coun,answer

def launch_personnality(texto,nombre,id):
    # save language and explain personality test
    lang = texto
    answer = 'Thanks for these basic details, from now we will do a quick personality test in order for me to know who you really are.\nFor each question, you will answer one digit from 1 to 5. The meanings are:\n1. Completely disagree\n2. Partially disagree\n3. Neutral\n4. Partially agree \n5. Completely agree'
    answer += '\n\nLet\'s begin!\n\n1/50: I am the life of the party'
    return lang,answer