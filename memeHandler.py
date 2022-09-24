# se encarga de los memes, no confundr con ele Meme Master, tomas eggsy sirio.
# Busca y guarda memes

#imports
import utils as u
import dataBaseImpl as db




################
#Dudas y comentarios
################
#duda: EL memehandler al final no hace nada, pasa de largo los parametros que recibe del bot a la base de datos implementada

#Entiendo igual que es util tenerlo si en el futuro quiero por ejemplo agregar una segunda base de datos

#la base de datos implementada se ocupa ella solita de cargar el archivo imagenes.csv donde estan los memes

#casi que el memehandler no quiere que corporate se de cuenta que no hace nada en la oficina y cobra mas que dataBaseImp.py

#Entiendo a dataBaseImpl como una simplificacion del pandas?

#Capaz algunas de las funciones que estan en dataBaseIMpl tendria que pasarselas al memeHandler?


#levanto la base de datos implementada
memeDataBase = db.baseDeDatos()


def sendRandomMeme(lista_tags=[]): #, df=imagenes_df):

    meme_id, tags = memeDataBase.getRandomMeme(lista_tags)

    return meme_id, tags


def sendMemeIndex(indice):
    meme_id, tags = memeDataBase.getMemeIndex(indice)
    return meme_id, tags


def addMeme(file_id, tags = []):
    
    memeDataBase.addMeme(file_id,tags)

    return None


def agregarTags(meme_id, tags):
    memeDataBase.addTags(meme_id, tags)

    return None