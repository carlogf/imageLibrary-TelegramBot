

#imports
import random as random



#funcion que manda strings de listas en una lista
def strToList(lista):
    if lista == '[]':
        return []
    else:
        lista=lista.strip("['").strip("']") #remuevo los corchetes
        ret=lista.split("', '")
    return ret



def pasarACaption(lista): #toma una lista de tags y devuelve el texto que va en el mensaje
    ret=''
    if len(lista)>3:
        lista=random.sample(lista,3)
    
    for t in lista:
        ret=ret + '#'+t + ' '
    
    ret.strip(' ') #quita el espacio del final
    
    return ret
