from config import TOKEN
from telegram.ext import Updater
from telegram.ext import (CallbackQueryHandler, CommandHandler,
                          ConversationHandler, Filters, MessageHandler)
from constants import *
from start_menu import *
from interrupt import *


updater = Updater(TOKEN)
dispatcher = updater.dispatcher


contact_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        MENU: [MessageHandler(Filters.text & ~Filters.command, main_menu)],
        MENU_ITEMS:[
            MessageHandler(Filters.text & ~Filters.command, wrong_message),
            MessageHandler(Filters.photo, wrong_message)
        ]
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)


dispatcher.add_handler(contact_handler)
print("started:", updater.bot.first_name)
updater.start_polling()
updater.idle()
