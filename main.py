import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot starting ...")

def start_command(update,context):
    update.message.reply_text('Type sth random')

def help_command(update,context):
    update.message.reply_text('If u need help , thug it out ho')


def handle_message(update,context):
    # Gets the input
    text = str(update.message.text).lower()
    # Processes it 
    response = R.sample_resp(text)
    #Replies to the user
    update.message.reply_text(response)

def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY,update_queue=None)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))

    dp.add_handler(MessageHandler(Filters.text,handle_message))
    
    dp.add_error_handler(error)

    updater.start_polling(7)

    updater.idle()

main()

