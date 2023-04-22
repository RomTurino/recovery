from telegram import Update
from telegram.ext import CallbackContext
import csv
import os

def init(update: Update, context: CallbackContext):
    username = update.effective_user.username
    filename = f'database/{username}.csv'
    context.user_data['file'] = filename
    if not os.path.exists('database'): # если не существует папки
        os.mkdir('database') # создаем папку
    if not os.path.exists(filename): # если не существует файла
        open(filename, 'w') # открыть файл для записи

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

