import csv
from telegram.ext import CallbackContext, ConversationHandler
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)
import random
import time

GO = 'Поехали'
GAME = 1
QUESTIONS_ON_ROUND = 6


def start(update: Update, context: CallbackContext):
    mark_up = [[GO]]
    keyboard = ReplyKeyboardMarkup(
        keyboard=mark_up,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=f'Нажми на кнопку "{GO}", поиграем!'
    )
    # update.message.reply_sticker(START_STICKER)
    update.message.reply_text(
        'Добро пожаловать в викторину😇! Выбирайте правильный ответ')
    update.message.reply_text(
        f'Чтобы начать, нажми на "{GO}"', reply_markup=keyboard)
    questions = read_csv()  # берем все вопросы
    random.shuffle(questions)  # перемешиваем вопросы
    
    questions = questions[:QUESTIONS_ON_ROUND]  # срез
    context.user_data["вопросы"] = questions  # сохранили в рюкзак
    context.user_data['right_answer'] = GO
    return GAME


def game(update: Update, context: CallbackContext):
    questions = context.user_data["вопросы"]  # берем из рюкзака вопросы
    
    user_answer = update.message.text
    right_answer = context.user_data['right_answer']
    if user_answer == GO:
        pass
    elif user_answer == right_answer:
        update.message.reply_photo(
            "http://risovach.ru/upload/2015/10/mem/vyv_94918784_orig_.jpg")
    else:
        update.message.reply_photo(
            'http://risovach.ru/upload/2016/04/mem/dibrov-vozmucshyon_111242784_orig_.jpg')

    if len(questions) == 0:
        update.message.reply_text('Вопросы закончились. Конец игры')
        # здесь часть вашего дз: подсчет очков
        return ConversationHandler.END
    
    answers = questions.pop()  # достаем последний вопрос из списка
    question_text = answers.pop(0)  # взяли текст вопроса
    right_answer = answers[0]  # первый ответ - правильный
    random.shuffle(answers) # перемешиваем ответы
    context.user_data['right_answer'] = right_answer # сохраняем правильный ответ
    mark_up = [answers[:2], answers[2:]]
    keyboard = ReplyKeyboardMarkup(
        keyboard=mark_up,
        resize_keyboard=True
    )

    time.sleep(1)
    update.message.reply_text(question_text, reply_markup=keyboard)

def end(update: Update, context: CallbackContext):  # точка выхода
    name = context.user_data['имя']
    update.message.reply_text(
        f"Значит, ты выбрал конец, {name}. Если хотите начать заново, нажмите /start")
    return ConversationHandler.END


def read_csv():
    # читать вопросы из файла
    with open('05_quiz\вопросы.csv', 'r', encoding='utf-8') as file:
        quest = list(csv.reader(file, delimiter='|'))
        return quest


def write_csv():
    # записать вопрос
    with open('05_quiz\вопросы.csv', 'a', encoding='utf-8') as file:
        worker = csv.writer(file, delimiter='|',
                            lineterminator='\n')  # \n - это перенос
        worker.writerow(['Какая столица Татарстана?',
                        'Казань', 'Астана', 'Елабуга', 'Челны'])
