import database
import greetings
import re

def q1(texto,nombre,id):
    r1 = int(texto)
    answer = '2/50: I feel little concern for others'
    return r1,answer

def q2(texto,nombre,id):
    r2 = int(texto)
    answer = '3/50: I am always prepared'
    return r2,answer

def q3(texto,nombre,id):
    r3 = int(texto)
    answer = '4/50: I get stressed out easily'
    return r3,answer

def q4(texto,nombre,id):
    r4 = int(texto)
    answer = '5/50: I have a rich vocabulary'
    return r4,answer

def q5(texto,nombre,id):
    r5 = int(texto)
    answer = '6/50: I don\'t talk a lot'
    return r5,answer

def q6(texto,nombre,id):
    r6 = int(texto)
    answer = '7/50: I am interested in people'
    return r6,answer

def q7(texto,nombre,id):
    r7 = int(texto)
    answer = '8/50: I leave my belongings around'
    return r7,answer

def q8(texto,nombre,id):
    r8 = int(texto)
    answer = '9/50: I am relaxed most of the time'
    return r8,answer

def q9(texto,nombre,id):
    r9 = int(texto)
    answer = '10/50: I have difficulty understanding abstract ideas'
    return r9,answer

def q10(texto,nombre,id):
    r10 = int(texto)
    answer = '11/50: I feel comfortable around people'
    return r10,answer

def q11(texto,nombre,id):
    r11 = int(texto)
    answer = '12/50: I insult people'
    return r11,answer

def q12(texto,nombre,id):
    r12 = int(texto)
    answer = '13/50: I pay attention to details'
    return r12,answer

def q13(texto,nombre,id):
    r13 = int(texto)
    answer = '14/50: I worry about things'
    return r13,answer

def q14(texto,nombre,id):
    r14 = int(texto)
    answer = '15/50: I have a vivid imagination'
    return r14,answer

def q15(texto,nombre,id):
    r15 = int(texto)
    answer = '16/50: I keep in the background'
    return r15,answer

def q16(texto,nombre,id):
    r16 = int(texto)
    answer = '17/50: I sympathize with others\' feelings'
    return r16,answer

def q17(texto,nombre,id):
    r17 = int(texto)
    answer = '18/50: I make a mess of things'
    return r17,answer

def q18(texto,nombre,id):
    r18 = int(texto)
    answer = '19/50: I seldom feel blue'
    return r18,answer

def q19(texto,nombre,id):
    r19 = int(texto)
    answer = '20/50: I am not interested in abstract ideas'
    return r19,answer

def q20(texto,nombre,id):
    r20 = int(texto)
    answer = '21/50: I start conversations'
    return r20,answer

def q21(texto,nombre,id):
    r21 = int(texto)
    answer = '22/50: I am not interested in other people\'s problems'
    return r21,answer

def q22(texto,nombre,id):
    r22 = int(texto)
    answer = '23/50: I get chores done right away'
    return r22,answer

def q23(texto,nombre,id):
    r23 = int(texto)
    answer = '24/50: I am easily disturbed'
    return r23,answer

def q24(texto,nombre,id):
    r24 = int(texto)
    answer = '25/50: I have excellent ideas'
    return r24,answer

def q25(texto,nombre,id):
    r25 = int(texto)
    answer = '26/50: I have little to say'
    return r25,answer

def q26(texto,nombre,id):
    r26 = int(texto)
    answer = '27/50: I have a soft heart'
    return r26,answer

def q27(texto,nombre,id):
    r27 = int(texto)
    answer = '28/50: I often forget to put things back in their proper place'
    return r27,answer

def q28(texto,nombre,id):
    r28 = int(texto)
    answer = '29/50: I get upset easily'
    return r28,answer

def q29(texto,nombre,id):
    r29 = int(texto)
    answer = '30/50: I do not have a good imagination'
    return r29,answer

def q30(texto,nombre,id):
    r30 = int(texto)
    answer = '31/50: I talk to a lot of different people at parties'
    return r30,answer

def q31(texto,nombre,id):
    r31 = int(texto)
    answer = '32/50: I am not really interested in others'
    return r31,answer

def q32(texto,nombre,id):
    r32 = int(texto)
    answer = '33/50: I like order'
    return r32,answer

def q33(texto,nombre,id):
    r33 = int(texto)
    answer = '34/50: I change my mood a lot'
    return r33,answer

def q34(texto,nombre,id):
    r34 = int(texto)
    answer = '35/50: I am quick to understand things'
    return r34,answer

def q35(texto,nombre,id):
    r35 = int(texto)
    answer = '36/50: I don\'t like to draw attention to myself'
    return r35,answer

def q36(texto,nombre,id):
    r36 = int(texto)
    answer = '37/50: I take time out for others'
    return r36,answer

def q37(texto,nombre,id):
    r37 = int(texto)
    answer = '38/50: I shirk my duties'
    return r37,answer

def q38(texto,nombre,id):
    r38 = int(texto)
    answer = '39/50: I have frequent mood swings'
    return r38,answer

def q39(texto,nombre,id):
    r39 = int(texto)
    answer = '40/50: I use difficult words'
    return r39,answer

def q40(texto,nombre,id):
    r40 = int(texto)
    answer = '41/50: I don\'t mind being the center of attention'
    return r40,answer

def q41(texto,nombre,id):
    r41 = int(texto)
    answer = '42/50: I feel others\' emotions'
    return r41,answer

def q42(texto,nombre,id):
    r42 = int(texto)
    answer = '43/50: I follow a schedule'
    return r42,answer

def q43(texto,nombre,id):
    r43 = int(texto)
    answer = '44/50: I get irritated easily'
    return r43,answer

def q44(texto,nombre,id):
    r44 = int(texto)
    answer = '45/50: I spend time reflecting on things'
    return r44,answer

def q45(texto,nombre,id):
    r45 = int(texto)
    answer = '46/50: I am quiet around strangers'
    return r45,answer

def q46(texto,nombre,id):
    r46 = int(texto)
    answer = '47/50: I make people feel at ease'
    return r46,answer

def q47(texto,nombre,id):
    r47 = int(texto)
    answer = '48/50: I am exacting in my work'
    return r47,answer

def q48(texto,nombre,id):
    r48 = int(texto)
    answer = '49/50: I often feel blue'
    return r48,answer

def q49(texto,nombre,id):
    r49 = int(texto)
    answer = '50/50: I am full of ideas'
    return r49,answer

def q50(texto,nombre,id):
    r50 = int(texto)
    answer = 'Ok that\'s it! Do you want to know who you are ?'
    return r50,answer

def compute_results(res):
    # store questions in their respective personality trait
    extraversion = [[res[0],res[10],res[20],res[30],res[40]] , [res[5],res[15],res[25],res[35],res[45]]]
    agreeableness = [[res[6],res[16],res[26],res[36],res[41],res[46]] , [res[1],res[11],res[21],res[31]]]
    conscientiousness = [[res[2],res[12],res[22],res[32],res[42],res[47]] , [res[7],res[17],res[27],res[37]]]
    emotional_stability = [[res[8],res[18]] , [res[3],res[13],res[23],res[28],res[33],res[38],res[43],res[48]]]
    intellect = [[res[4],res[14],res[24],res[34],res[39],res[44],res[49]] , [res[9],res[19],res[29]]]
    
    # re compute negative keyed items
    def re_compute(item):
        if item==1:
            return 5
        elif item==2:
            return 4
        elif item==4:
            return 2
        elif item==5:
            return 1
        else:
            return 3
    
    extraversion[1] = [re_compute(i) for i in extraversion[1]]
    agreeableness[1] = [re_compute(i) for i in agreeableness[1]]
    conscientiousness[1] = [re_compute(i) for i in conscientiousness[1]]
    emotional_stability[1] = [re_compute(i) for i in emotional_stability[1]]
    intellect[1] = [re_compute(i) for i in intellect[1]]

    ext = sum(extraversion[0])+sum(extraversion[1])
    agr = sum(agreeableness[0])+sum(agreeableness[1])
    cons = sum(conscientiousness[0])+sum(conscientiousness[1])
    emo = sum(emotional_stability[0])+sum(emotional_stability[1])
    intel = sum(intellect[0])+sum(intellect[1])

    return [ext,agr,cons,emo,intel]


def personality_to_genres(res):
    genres = ""
    if res[0] <= 25: # low extraversion
        genres += 'Music,War,Mystery,Film-Noir,'
    elif res[0] > 25: # high extraversion
        genres += 'Action,Adventure,Comedy,Sport,Musical,Talk-Show,'
    
    if res[1] <= 25: # low agreeableness
        genres += 'Thriller,War,Crime,Horror,'
    elif res[1] > 25: # high agreeableness
        genres += 'Comedy,Family,Romance,Sport,Game-Show,'
    
    if res[2] <= 25: # low conscientiousness
        genres += 'Thriller,Drama,Crime,Reality-TV,Film-Noir,'
    elif res[2] > 25: # high conscientiousness
        genres += 'Family,Romance,Documentary,'
    
    if res[3] <= 25: # low emotional_stability
        genres += 'Action,Thriller,Drama,Crime,Romance,Horror,Reality-TV,'
    elif res[3] > 25: # high emotional_stability
        genres += 'Family,Musical,'
    
    if res[4] <= 25: # low imagination
        genres += 'Western,Biography,History,Sport,Documentary,News,'
    elif res[4] > 25: # high imagination
        genres += 'Adventure,Sci-Fi,Animation,Fantasy,Mystery,Short,'
    
    return genres


def results(texto,nombre,id,res):
    r = compute_results(res)
    answer = 'Here are your scores:\n'
    answer += '\n- Extraversion score: %d' % (r[0])
    answer += '\n- Agreeableness score: %d' % (r[1])
    answer += '\n- Conscientiousness score: %d' % (r[2])
    answer += '\n- Emotional_stability score: %d' % (r[3])
    answer += '\n- Intellect score: %d' % (r[4])
    print(r)
    database.updateUser(id,nombre,'personality',r)
    database.updateUser(id,nombre,'genres',personality_to_genres(r))
    answer += '\n(Type \Ok to continue)'    
    return answer,r
