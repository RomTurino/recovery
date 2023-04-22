from telegram import  Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
from stickers import *


def cancel(update: Update, context: CallbackContext):
    update.message.reply_sticker(
        CANCEL_STICKER)
    update.message.reply_text('Спасибо за использование списка задач, мастер!',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def wrong_message(update: Update, context: CallbackContext):
    update.message.reply_sticker(WRONG_COMMAND_STICKER)
    update.message.reply_text('Упс! Такой команды не существует')
