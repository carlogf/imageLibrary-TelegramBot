#Implementacion de la base de datos

#la onda es que podia implementarla en el meme handler
#pero al final, la implemento aparte con las mismas funciones y ya, asi el memehandler no esta preocu
#pandose con el pandas ni nada, toma el filepath, lo carga con esta clase, y lo usa y listo

import pandas as pd
import utils as u

#Duda. esta es la implementacion de mi base de datos que ya tengo, no? Puedo poner variables globales con los nombres de las columnas y el filePath?

#Duda. Parece poco prolijo guardarlas como variables globales en el archivo .py

filePath = 'images.csv'

#guardo los nombres de las columnas en variables
file_id = 'file_id'
hashtags = 'hashtags' #la columan con tags

class baseDeDatos:
    def __init__(self):
        self.df = pd.read_csv(filePath)
        self.df[hashtags] = self.df[hashtags].apply(u.strToList)

        #creo que el unico atributo que tiene es el dataframe
    

    def getRandomMeme(self, lista_tags = []):

        if lista_tags != []:
            m=[(all(tag in tags_existentes for tag in lista_tags)) for tags_existentes in self.df[hashtags]] 
            #m parece ser una lista de true y false si en cada meme estan los tags que piden, no me acuerdo bien jeje

            def_aux = self.df[m]
            ret = def_aux.sample()
        
        else:
            ret = self.df.sample()
        
        n = ret.index[0] #recupero el indice que lo necesito

        return ret[file_id][n], ret[hashtags][n]

    
    def getMemeIndex(self,indice):
        
        foto = self.df.loc[indice][file_id]
        tags = self.df.loc[indice][hashtags]

        return foto, tags


    def addMeme(self, new_meme_id, tags = []):
        self.df.loc[len(self.df.index)] = [new_meme_id,tags]

        self.saveToCSV()
        

    def addTags(self, meme_id, tags):
        
        #ubico el indice
        indice = self.df[self.df[file_id] == meme_id].index[0]

        for tag in tags:
            self.df.loc[indice][hashtags].append(tag)
        
        #guardo en el csv
        self.saveToCSV()
        

    def saveToCSV(self):
        self.df.to_csv(filePath, index = False)