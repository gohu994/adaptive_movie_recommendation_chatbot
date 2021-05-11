import os
import sys
import urllib.request, json 
from urllib.request import urlopen
import end
import json
import requests
import re

import database
import greetings
import personality
import questions
import recommend
import end



#Variables para el Token y la URL del chatbot
TOKEN = "1741996807:AAGXqTzr2WrHFFzw5_PWz22h3toqbiiZ79Q"
URL = "https://api.telegram.org/bot" + TOKEN + "/"

def update(offset):
    #Llamar al metodo getUpdates del bot, utilizando un offset
    respuesta = requests.get(URL + "getUpdates" + "?offset=" + str(offset))
    #Telegram devolvera todos los mensajes con id IGUAL o SUPERIOR al offset
 
 
    #Decodificar la respuesta recibida a formato UTF8
    mensajes_js = respuesta.content.decode("utf8")
 
    #Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)
 
    #Devolver este diccionario
    return mensajes_diccionario
 
 
def leer_mensaje(mensaje):
    #Extraer el texto, nombre de la persona e id del último mensaje recibido
    texto = mensaje["message"]["text"]
    persona = mensaje["message"]["from"]["first_name"]
    id_chat = mensaje["message"]["chat"]["id"]

    #Calcular el identificador unico del mensaje para calcular el offset
    id_update = mensaje["update_id"]
 
    #Devolver las dos id, el nombre y el texto del mensaje
    return id_chat, persona, texto, id_update
 
def enviar_mensaje(idchat, texto):
    #Llamar el metodo sendMessage del bot, passando el texto y la id del chat
    requests.get(URL + "sendMessage?text=" + texto + "&chat_id=" + str(idchat))
    return 0
 

# --------------------- ADD ANSWER PROCESSING FUNCTIONS WITH 'answer+=module.feature ------------------------
def process_message(texto,nombre,ID,stage):
    #stage = 0
    answer =''
    if stage == 0:
        answer = greetings.greet(texto,nombre)
        if answer == "I beg your pardon? Type '/start' to begin the experience":
            return 0,answer
        stage += 1
        return stage,answer
    elif stage == 1:
        if database.isKnown(ID,nombre) == False:
            answer = greetings.greet_answer(texto,nombre,ID)
            answer += greetings.begin_details_age(texto,nombre,ID)
            stage += 1
            return stage,answer
        else:
            answer = greetings.greet_answer(texto,nombre,ID)
            stage = 64

    elif stage == 2:
        age,answer = greetings.ask_country(texto,nombre,ID)
        stage += 1
        return stage,answer,age
    
    elif stage == 3:
        country,answer = greetings.ask_language(texto,nombre,ID)
        stage += 1
        return stage,answer,country
    
    elif stage == 4:
        language,answer = greetings.launch_personnality(texto,nombre,ID)
        stage += 1
        return stage,answer,language
    
    elif stage == 5:
        r1,answer = personality.q1(texto,nombre,ID)
        stage += 1
        return stage,answer,r1
    
    elif stage == 6:
        r2,answer = personality.q2(texto,nombre,ID)
        stage += 1
        return stage,answer,r2

    elif stage == 7:
        r3,answer = personality.q3(texto,nombre,ID)
        stage += 1
        return stage,answer,r3

    elif stage == 8:
        r4,answer = personality.q4(texto,nombre,ID)
        stage += 1
        return stage,answer,r4

    elif stage == 9:
        r5,answer = personality.q5(texto,nombre,ID)
        stage += 1
        return stage,answer,r5

    elif stage == 10:
        r6,answer = personality.q6(texto,nombre,ID)
        stage += 1
        return stage,answer,r6
    
    elif stage == 11:
        r7,answer = personality.q7(texto,nombre,ID)
        stage += 1
        return stage,answer,r7
    
    elif stage == 12:
        r8,answer = personality.q8(texto,nombre,ID)
        stage += 1
        return stage,answer,r8

    elif stage == 13:
        r9,answer = personality.q9(texto,nombre,ID)
        stage += 1
        return stage,answer,r9
    
    elif stage == 14:
        r10,answer = personality.q10(texto,nombre,ID)
        stage += 1
        return stage,answer,r10
    
    elif stage == 15:
        r11,answer = personality.q11(texto,nombre,ID)
        stage += 1
        return stage,answer,r11
    
    elif stage == 16:
        r12,answer = personality.q12(texto,nombre,ID)
        stage += 1
        return stage,answer,r12
    
    elif stage == 17:
        r13,answer = personality.q13(texto,nombre,ID)
        stage += 1
        return stage,answer,r13
    
    elif stage == 18:
        r14,answer = personality.q14(texto,nombre,ID)
        stage += 1
        return stage,answer,r14
    
    elif stage == 19:
        r15,answer = personality.q15(texto,nombre,ID)
        stage += 1
        return stage,answer,r15
    
    elif stage == 20:
        r16,answer = personality.q16(texto,nombre,ID)
        stage += 1
        return stage,answer,r16
    
    elif stage == 21:
        r17,answer = personality.q17(texto,nombre,ID)
        stage += 1
        return stage,answer,r17
    
    elif stage == 22:
        r18,answer = personality.q18(texto,nombre,ID)
        stage += 1
        return stage,answer,r18
    
    elif stage == 23:
        r19,answer = personality.q19(texto,nombre,ID)
        stage += 1
        return stage,answer,r19
    
    elif stage == 24:
        r20,answer = personality.q20(texto,nombre,ID)
        stage += 1
        return stage,answer,r20
    
    elif stage == 25:
        r21,answer = personality.q21(texto,nombre,ID)
        stage += 1
        return stage,answer,r21
    
    elif stage == 26:
        r22,answer = personality.q22(texto,nombre,ID)
        stage += 1
        return stage,answer,r22
    
    elif stage == 27:
        r23,answer = personality.q23(texto,nombre,ID)
        stage += 1
        return stage,answer,r23
    
    elif stage == 28:
        r24,answer = personality.q24(texto,nombre,ID)
        stage += 1
        return stage,answer,r24
    
    elif stage == 29:
        r25,answer = personality.q25(texto,nombre,ID)
        stage += 1
        return stage,answer,r25
    
    elif stage == 30:
        r26,answer = personality.q26(texto,nombre,ID)
        stage += 1
        return stage,answer,r26
    
    elif stage == 31:
        r27,answer = personality.q27(texto,nombre,ID)
        stage += 1
        return stage,answer,r27
    
    elif stage == 32:
        r28,answer = personality.q28(texto,nombre,ID)
        stage += 1
        return stage,answer,r28
    
    elif stage == 33:
        r29,answer = personality.q29(texto,nombre,ID)
        stage += 1
        return stage,answer,r29
    
    elif stage == 34:
        r30,answer = personality.q30(texto,nombre,ID)
        stage += 1
        return stage,answer,r30
    
    elif stage == 35:
        r31,answer = personality.q31(texto,nombre,ID)
        stage += 1
        return stage,answer,r31
    
    elif stage == 36:
        r32,answer = personality.q32(texto,nombre,ID)
        stage += 1
        return stage,answer,r32
    
    elif stage == 37:
        r33,answer = personality.q33(texto,nombre,ID)
        stage += 1
        return stage,answer,r33
    
    elif stage == 38:
        r34,answer = personality.q34(texto,nombre,ID)
        stage += 1
        return stage,answer,r34
    
    elif stage == 39:
        r35,answer = personality.q35(texto,nombre,ID)
        stage += 1
        return stage,answer,r35
    
    elif stage == 40:
        r36,answer = personality.q36(texto,nombre,ID)
        stage += 1
        return stage,answer,r36
    
    elif stage == 41:
        r37,answer = personality.q37(texto,nombre,ID)
        stage += 1
        return stage,answer,r37
    
    elif stage == 42:
        r38,answer = personality.q38(texto,nombre,ID)
        stage += 1
        return stage,answer,r38
    
    elif stage == 43:
        r39,answer = personality.q39(texto,nombre,ID)
        stage += 1
        return stage,answer,r39
    
    elif stage == 44:
        r40,answer = personality.q40(texto,nombre,ID)
        stage += 1
        return stage,answer,r40
    
    elif stage == 45:
        r41,answer = personality.q41(texto,nombre,ID)
        stage += 1
        return stage,answer,r41
    
    elif stage == 46:
        r42,answer = personality.q42(texto,nombre,ID)
        stage += 1
        return stage,answer,r42
    
    elif stage == 47:
        r43,answer = personality.q43(texto,nombre,ID)
        stage += 1
        return stage,answer,r43
    
    elif stage == 48:
        r44,answer = personality.q44(texto,nombre,ID)
        stage += 1
        return stage,answer,r44
    
    elif stage == 49:
        r45,answer = personality.q45(texto,nombre,ID)
        stage += 1
        return stage,answer,r45
    
    elif stage == 50:
        r46,answer = personality.q46(texto,nombre,ID)
        stage += 1
        return stage,answer,r46
    
    elif stage == 51:
        r47,answer = personality.q47(texto,nombre,ID)
        stage += 1
        return stage,answer,r47
    
    elif stage == 52:
        r48,answer = personality.q48(texto,nombre,ID)
        stage += 1
        return stage,answer,r48
    
    elif stage == 53:
        r49,answer = personality.q49(texto,nombre,ID)
        stage += 1
        return stage,answer,r49
    
    elif stage == 54:
        r50,answer = personality.q50(texto,nombre,ID)
        stage += 1
        return stage,answer,r50
    
    elif stage == 55:
        stage += 1
        return stage
    
    if stage == 56:
        answer += '\n\n'+questions.ask_Netflix(texto,nombre,ID)
    
    elif stage == 57:
        answer,netflix = questions.ask_Hulu(texto,nombre,ID)
        stage += 1
        return stage,answer,netflix
    
    elif stage == 58:
        answer,hulu = questions.ask_Prime(texto,nombre,ID)
        stage += 1
        return stage,answer,hulu
    
    elif stage == 59:
        answer,prime = questions.ask_Disney(texto,nombre,ID)
        stage += 1
        return stage,answer,prime

    elif stage == 60:
        answer,disney = questions.performing(texto,nombre,ID)
        stage += 1
        return stage,answer,disney
        
    elif stage == 61:
        stage += 1
        return stage

    elif stage == 62:
        answer = questions.ask_recentness(texto,nombre,ID)
        stage += 1
        return stage,answer
    
    elif stage == 63:
        answer = questions.ask_other(texto,nombre,ID)
        stage += 5 # add any number to jump up to 'how many movies do you want me to suggest ?'
    
    elif stage == 64:
        answer += recommend.ask_seen(texto,nombre,ID)
        stage += 1
        return stage,answer

    elif stage == 65:
        if re.findall('[0-9]+', texto) != []:
            answer = recommend.ask_liked(texto,nombre,ID)
            stage += 1
            return stage,answer
        else:
            answer = 'Please type at least one of the above numbers.'
            return stage,answer

    elif stage == 66:
        if re.findall('[0-9]+', texto) != []:
            answer = recommend.ask_disliked(texto,nombre,ID)
            stage += 1
            return stage,answer
        else:
            answer = 'Please type at least one of the above numbers.'
            return stage,answer
    
    elif stage == 67:
        if re.findall('[0-9]+', texto) != []:
            answer = recommend.process_feedback(texto,nombre,ID)
            stage += 1
            return stage,answer
        else:
            answer = 'Please type at least one of the above numbers.'
            return stage,answer



    elif stage == 68:
        answer += "How many movies do you want me to suggest ?"

    elif stage == 69:
        stage += 1
        return stage
    
    elif stage == 70:
        stage += 1
        return stage



    #else:
    #    answer = end.bye(texto,nombre,id)
    #    if answer != '':
    #        return -1,answer
    
    stage += 1
    return stage,answer

 
#Variable para almacenar la ID del ultimo mensaje procesado
ultima_id = 0

stage = 0
n_best = 0
platforms = []

while(stage >= 0):
    mensajes_diccionario = update(ultima_id)
    
    with open('updates.json','w') as json_file:
        json.dump(mensajes_diccionario,json_file,indent=4, sort_keys=True)
    
    for i in mensajes_diccionario["result"]:
        if ('message' in i.keys()):
            #Llamar a la funcion "leer_mensaje()"
            id_chat, nombre, texto, id_update = leer_mensaje(i)
            if id_chat != 1690350938:
                continue
            #Si la ID del mensaje es mayor que el ultimo, se guarda la ID + 1
            if id_update > (ultima_id-1):
                ultima_id = id_update + 1

            answer = ''
            print(stage,texto)
            
            if stage == 2:
                stage,answer,age = process_message(texto,nombre,id_chat,stage)
            elif stage == 3:
                stage,answer,country = process_message(texto,nombre,id_chat,stage)
            elif stage == 4:
                stage,answer,language = process_message(texto,nombre,id_chat,stage)
                res = database.newUser(id_chat,nombre,age,country,language)
            elif stage == 5:
                res = []
                stage,answer,r1 = process_message(texto,nombre,id_chat,stage)
                res.append(r1)
            elif stage == 6:
                stage,answer,r2 = process_message(texto,nombre,id_chat,stage)
                res.append(r2)
            elif stage == 7:
                stage,answer,r3 = process_message(texto,nombre,id_chat,stage)
                res.append(r3)
            elif stage == 8:
                stage,answer,r4 = process_message(texto,nombre,id_chat,stage)
                res.append(r4)
            elif stage == 9:
                stage,answer,r5 = process_message(texto,nombre,id_chat,stage)
                res.append(r5)
            elif stage == 10:
                stage,answer,r6 = process_message(texto,nombre,id_chat,stage)
                res.append(r6)
            elif stage == 11:
                stage,answer,r7 = process_message(texto,nombre,id_chat,stage)
                res.append(r7)
            elif stage == 12:
                stage,answer,r8 = process_message(texto,nombre,id_chat,stage)
                res.append(r8)
            elif stage == 13:
                stage,answer,r9 = process_message(texto,nombre,id_chat,stage)
                res.append(r9)
            elif stage == 14:
                stage,answer,r10 = process_message(texto,nombre,id_chat,stage)
                res.append(r10)
            elif stage == 15:
                stage,answer,r11 = process_message(texto,nombre,id_chat,stage)
                res.append(r11)
            elif stage == 16:
                stage,answer,r12 = process_message(texto,nombre,id_chat,stage)
                res.append(r12)
            elif stage == 17:
                stage,answer,r13 = process_message(texto,nombre,id_chat,stage)
                res.append(r13)
            elif stage == 18:
                stage,answer,r14 = process_message(texto,nombre,id_chat,stage)
                res.append(r14)
            elif stage == 19:
                stage,answer,r15 = process_message(texto,nombre,id_chat,stage)
                res.append(r15)
            elif stage == 20:
                stage,answer,r16 = process_message(texto,nombre,id_chat,stage)
                res.append(r16)
            elif stage == 21:
                stage,answer,r17 = process_message(texto,nombre,id_chat,stage)
                res.append(r17)
            elif stage == 22:
                stage,answer,r18 = process_message(texto,nombre,id_chat,stage)
                res.append(r18)
            elif stage == 23:
                stage,answer,r19 = process_message(texto,nombre,id_chat,stage)
                res.append(r19)
            elif stage == 24:
                stage,answer,r20 = process_message(texto,nombre,id_chat,stage)
                res.append(r20)
            elif stage == 25:
                stage,answer,r21 = process_message(texto,nombre,id_chat,stage)
                res.append(r21)
            elif stage == 26:
                stage,answer,r22 = process_message(texto,nombre,id_chat,stage)
                res.append(r22)
            elif stage == 27:
                stage,answer,r23 = process_message(texto,nombre,id_chat,stage)
                res.append(r23)
            elif stage == 28:
                stage,answer,r24 = process_message(texto,nombre,id_chat,stage)
                res.append(r24)
            elif stage == 29:
                stage,answer,r25 = process_message(texto,nombre,id_chat,stage)
                res.append(r25)
            elif stage == 30:
                stage,answer,r26 = process_message(texto,nombre,id_chat,stage)
                res.append(r26)
            elif stage == 31:
                stage,answer,r27 = process_message(texto,nombre,id_chat,stage)
                res.append(r27)
            elif stage == 32:
                stage,answer,r28 = process_message(texto,nombre,id_chat,stage)
                res.append(r28)
            elif stage == 33:
                stage,answer,r29 = process_message(texto,nombre,id_chat,stage)
                res.append(r29)
            elif stage == 34:
                stage,answer,r30 = process_message(texto,nombre,id_chat,stage)
                res.append(r30)
            elif stage == 35:
                stage,answer,r31 = process_message(texto,nombre,id_chat,stage)
                res.append(r31)
            elif stage == 36:
                stage,answer,r32 = process_message(texto,nombre,id_chat,stage)
                res.append(r32)
            elif stage == 37:
                stage,answer,r33 = process_message(texto,nombre,id_chat,stage)
                res.append(r33)
            elif stage == 38:
                stage,answer,r34 = process_message(texto,nombre,id_chat,stage)
                res.append(r34)
            elif stage == 39:
                stage,answer,r35 = process_message(texto,nombre,id_chat,stage)
                res.append(r35)
            elif stage == 40:
                stage,answer,r36 = process_message(texto,nombre,id_chat,stage)
                res.append(r36)
            elif stage == 41:
                stage,answer,r37 = process_message(texto,nombre,id_chat,stage)
                res.append(r37)
            elif stage == 42:
                stage,answer,r38 = process_message(texto,nombre,id_chat,stage)
                res.append(r38)
            elif stage == 43:
                stage,answer,r39 = process_message(texto,nombre,id_chat,stage)
                res.append(r39)
            elif stage == 44:
                stage,answer,r40 = process_message(texto,nombre,id_chat,stage)
                res.append(r40)
            elif stage == 45:
                stage,answer,r41 = process_message(texto,nombre,id_chat,stage)
                res.append(r41)
            elif stage == 46:
                stage,answer,r42 = process_message(texto,nombre,id_chat,stage)
                res.append(r42)
            elif stage == 47:
                stage,answer,r43 = process_message(texto,nombre,id_chat,stage)
                res.append(r43)
            elif stage == 48:
                stage,answer,r44 = process_message(texto,nombre,id_chat,stage)
                res.append(r44)
            elif stage == 49:
                stage,answer,r45 = process_message(texto,nombre,id_chat,stage)
                res.append(r45)
            elif stage == 50:
                stage,answer,r46 = process_message(texto,nombre,id_chat,stage)
                res.append(r46)
            elif stage == 51:
                stage,answer,r47 = process_message(texto,nombre,id_chat,stage)
                res.append(r47)
            elif stage == 52:
                stage,answer,r48 = process_message(texto,nombre,id_chat,stage)
                res.append(r48)
            elif stage == 53:
                stage,answer,r49 = process_message(texto,nombre,id_chat,stage)
                res.append(r49)
            elif stage == 54:
                stage,answer,r50 = process_message(texto,nombre,id_chat,stage)
                res.append(r50)
            elif stage == 55:
                answer,r = personality.results(texto,nombre,id_chat,res)
                stage += 1
            #elif stage == 56:
            #    stage,answer = process_message(texto,nombre,id_chat,stage)
            elif stage == 57:
                stage,answer,netflix = process_message(texto,nombre,id_chat,stage)
                platforms.append(netflix)
            elif stage == 58:
                stage,answer,hulu = process_message(texto,nombre,id_chat,stage)
                platforms.append(hulu)
            elif stage == 59:
                stage,answer,prime = process_message(texto,nombre,id_chat,stage)
                platforms.append(prime)
            elif stage == 60:
                stage,answer,disney = process_message(texto,nombre,id_chat,stage)
                platforms.append(disney)
            elif stage == 61:
                if platforms == [0,0,0,0]:
                    answer += 'As you don\'t have access to any streaming platform, we cannot guarantee that you will have access to the recommended movies'
                answer += '\n'+questions.platforms_saved(texto,nombre,id_chat,platforms)
                stage += 1
            elif stage == 69:
                answer,nb = questions.ask_n_best(texto,nombre,id_chat)
                stage += 1
                n_best = nb
            elif stage == 70:
                recom,answer = recommend.take_n_best(texto,nombre,id_chat,n_best)
                stage += 1
            elif stage == 71:
                if re.search('bye', texto, re.IGNORECASE)!=None:
                    answer = end.bye(texto,nombre,id)
                    stage = -1
                elif re.search('start', texto, re.IGNORECASE)!=None:
                    stage = 0
                    answer = 'Please now type \'/start\' to begin again'
                else:
                    answer = 'I beg your pardon ?'
                

            else:
                stage,answer = process_message(texto,nombre,id_chat,stage)

            if answer!='':
                enviar_mensaje(id_chat,answer)
                if stage == -1:
                    break
            else:
                continue
        else:
            pass
            
        
        
            

    #Vaciar el diccionario
    mensajes_diccionario = []

