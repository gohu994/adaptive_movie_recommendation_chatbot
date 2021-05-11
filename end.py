import re
def bye(texto,nombre,id):
    answer = ''
    if re.search('bye', texto, re.IGNORECASE)!=None:
        answer = 'Bye, %s! I hope you\'ll have a great time watching your movie!' % (nombre)
    return answer