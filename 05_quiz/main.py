from config import TOKEN
from telegram.ext import (
    Updater,
    Filters,
    MessageHandler,
    CommandHandler,
    ConversationHandler
)
from functions import *


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)], # точка входа в разговор
    states={ # этапы разговора
        GAME: [MessageHandler(Filters.text & ~Filters.command, game)]
        },
    fallbacks=[CommandHandler('end', end)] # точка выхода из разговора
)


dispatcher.add_handler(conv_handler)

print('Сервер запущен!')
updater.start_polling()
updater.idle()  # ctrl + C
