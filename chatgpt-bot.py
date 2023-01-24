
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram
import os
import sys
#pip install openai
import openai

#==============================================opties=================================================
#api key voor de openai text generator
openai.api_key = open("ai_key.txt").readline().rstrip()

#credits @ https://github.com/raspiuser1/
#token that can be generated talking with @BotFather on telegram, put this in key.txt
my_token=open("key.txt").readline().rstrip()

#==============================================================================================================

updater = Updater(my_token,use_context=True)
bot = telegram.Bot(token=my_token)

def help(update: Update, context: CallbackContext):
	update.message.reply_text(""" ======Options YT subtitle Bot======
Credits @ https://github.com/raspiuser1

/ai [keywords or whatever you want to ask at chatgpt] 

""")

def ai(update: Update, context: CallbackContext):
    fr44 = update.message.text[4:]
    response = openai.Completion.create(model="text-davinci-003", prompt=fr44, temperature=1, max_tokens=1000)
    #update.message.reply_text(json.dumps(response, indent=4))
    update.message.reply_text(response["choices"][0]["text"])
    


def txt(update: Update, context: CallbackContext):
        global tekst
        tekst += update.message.text + " "
        
    
def unknown_text(update: Update, context: CallbackContext):
    #uncomment if need to send to telegram:
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
    print("Sorry I can't recognize you , you said '%s'")

def main():
    #telegram options=================================================================================================
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('ai', ai))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, txt))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, txt)) # Filters out unknown commands
    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
    updater.start_polling(timeout=600)
    #updater.idle()
main()    
