from telegram.ext import CallbackContext, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
BEGIN, GAME = 1, 2
GO = "Вперед"


def start(update: Update, context: CallbackContext):
    mark_up = [[GO]] # разметка клавиатуры
    keyboard = ReplyKeyboardMarkup( # клавиатура в телеграме
        keyboard=mark_up,  # разметка клавиатуры
        resize_keyboard=True, # сжали размер
        one_time_keyboard = True, # 
        input_field_placeholder = f'Нажми на кнопку "{GO}", путник!' # текстовая подсказка
    )
    update.message.reply_text(
        f"""
        Ты любишь придумывать сказки? 
        Я очень люблю. Ты знаешь сказку как посадил дед репку?
        А кто помогал деду репку тянуть? Чтобы начать, нажми на кнопку {GO}!
        """,
        reply_markup=keyboard) # чтобы клавиатура показалась в чате
    return BEGIN


def begin(update: Update, context: CallbackContext):  # первый шаг разговора
    update.message.reply_text('''
                            Посадил дед репку. Выросла репка большая-пребольшая.
                            Стал дед репку из земли тянуть. 
                            Тянет-потянет - вытянуть не может.
                            Кого позвал дедка?
                            ''', reply_markup=ReplyKeyboardRemove()) # чтобы клавиатура исчезла полностью
    
    
    
    
    heroes = [["дедку"], ["дедка", "репку"]]
    context.user_data["heroes"] = heroes # сохраняем в словарь 
    update.message.reply_text('''
                            Посадил дед репку. Выросла репка большая-пребольшая.
                            Стал дед репку из земли тянуть. 
                            Тянет-потянет - вытянуть не может.
                            Кого позвал дедка?
                            ''', reply_markup=ReplyKeyboardRemove())
    return GAME # переход к следующему шагу


    


def end(update: Update, context: CallbackContext):  # точка выхода
    update.message.reply_text("Значит, ты выбрал конец")
    return ConversationHandler.END


# def game(update: Update, context: CallbackContext):
#     text = update.message.text
#     word = morph.parse(text)[0] # тег в Именительном падеже
#     nomn = word.inflect({'nomn'}).word
#     accs = word.inflect({'accs'}).word
#     update.message.reply_text(f'{nomn}, {accs}')
#     heroes = context.user_data["heroes"] # из рюкзака достаем героев
#     heroes[0].insert(0, nomn) # [["бабка", "дедку"], ["дедка", "репку"]]
#     heroes.insert(0, [accs]) #[["бабку"], ["бабка", "дедку"], ["дедка", "репку"]]
#     answer = f"Я {nomn}. Буду помогать. "      
#     for nom, acc in heroes[1:]:# убираем бабку в в.п. 
#         answer += f"{nom} за {acc}. "
#     answer += "Тянут-потянут - вытянуть не могут. Кого позовем еще?"    
#     update.message.reply_text(f'{answer}')
    
def game(update: Update, context: CallbackContext):    
    text = morph.parse(text)[0] # тег
    if text.tag.animacy == "anim": # если одушевленный
        nomn = text.inflect({'nomn'}).word  # именительный падеж
        accs = text.inflect({'accs'}).word  # винительный падеж
        heroes = context.user_data["heroes"] # достаем из рюкзака
        heroes[0].insert(0, nomn) # бабка за дедку
        heroes.insert(0, [accs]) 
        answer = f"Я {nomn}. Буду помогать. "      
        for nom, acc in heroes[1:]: 
            answer += f"{nom} за {acc}. "
        answer += "Тянут-потянут - вытянуть не могут. Кого позовем еще?"    
        update.message.reply_text(f'{answer}')
    else: #если персонаж неодушевленный 
        update.message.reply_text(f'Долго искали мы {text.normal_form}: ничего не нашли')


