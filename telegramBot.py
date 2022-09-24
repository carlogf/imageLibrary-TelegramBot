
#########################

#imports

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import logging


import utils as u
import telegramAPI_handler as tah
#########################


#Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


#Retrieving the token
f = open('token.txt','r')
myToken = f.readline()
f.close()

updater = Updater(token=myToken, use_context=True)

dispatcher = updater.dispatcher


###############################

#Funciones de respuesta


#funciones de comandos, reciben el comando del chat y llaman a la funcion correspondiente

def command_meme(update: Update, context: CallbackContext):
     
    photoToSend, texto = tah.send_meme(context.args)
    
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=photoToSend, caption = texto) 


def command_save(update: Update, context: CallbackContext):
    
    mensaje = tah.save_image(context.args)
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=mensaje)


def command_hashtag(update: Update, context: CallbackContext):

    mensaje = tah.add_hashtag(context.args)
    
    context.bot.send_message(chat_id=update.effective_chat.id, text = mensaje)


###################################
#Cada vez que mandan una foto al chat, el bot la guarda como ultima imagen enviada.

def handlePhotoSent(update: Update, context: CallbackContext):
    global mensaje_enviado #no me acuerdo porque defini esta variable como global
    mensaje_enviado=update.message
    
    photoid = mensaje_enviado.photo[-1].file_id
    tah.photo_sent_in_chat(photoid)



#defino handlers. A veces los defino en una variable a veces los defino en el dispatcher
photo_handler = MessageHandler(Filters.photo, handlePhotoSent)


#dispatchers
updater.dispatcher.add_handler(CommandHandler('meme', command_meme))
updater.dispatcher.add_handler(photo_handler)
updater.dispatcher.add_handler(CommandHandler('save',command_save))
updater.dispatcher.add_handler(CommandHandler('hashtag',command_hashtag))


updater.start_polling()

