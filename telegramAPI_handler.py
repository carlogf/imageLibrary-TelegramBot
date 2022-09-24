#Aca van las funciones que se ejecutan cuando llega un comando del chat. La idea es que en telegramBot solo esten las funciones de la API y que llame a las funciones de aca. Esto deberia modulizar todo.

#imports
import memeHandler as juan
import utils as u


# Class that keeps track of the last image sent
class LastSent:
    def __init__(self,fileId: str):
        lastSent = fileId

ultima_foto = LastSent('')



def send_meme(texto_crudo): #manda el meme que pidio el usuario
    
    parametro=' '.join(texto_crudo)

    if parametro.isdigit():
        photoToSend,tags = juan.sendMemeIndex(int(parametro))
    
    else:
        parametro = parametro.split()
        photoToSend, tags = juan.sendRandomMeme(parametro)
    
    ultima_foto.lastSent = photoToSend

    return photoToSend, u.pasarACaption(tags)   


def photo_sent_in_chat(photoid):
    
    #actualizo ultima foto
    ultima_foto.lastSent = photoid

    #esto lo podria cambiar cuando quiero que guarde todas las fotos que envie, para armar la datbase por ejemplo
    if False:
        addMeme(u.ultima_foto.lastSent, tags = [])
        print('foto guaradada, file id' +  str(photoid[-10:-1]))        


def save_image(texto_crudo):

    if ultima_foto.lastSent == '':
       mensaje = "no hay foto que guardar"

    
    else:
        hashtags=' '.join(texto_crudo) #el texto en crudo
        hashtags = hashtags.split()

        juan.addMeme(ultima_foto.lastSent, tags = hashtags)
        
        mensaje = "Guardada con tags " + str(hashtags)
    
    return mensaje

def add_hashtag(texto_crudo):

    hashtags = ' '.join(texto_crudo) #el texto en crudo
    hashtags = hashtags.split()
    print(hashtags)
    
    #foto a agregarle los tags:
    foto = ultima_foto.lastSent

    juan.agregarTags(foto,hashtags)
    return 'Tags agregadas'