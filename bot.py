import telebot
from bot_logic import generate
from bot_logic import flip
from bot_logic import phrases

bot = telebot.TeleBot('7719514735:AAEPJIkPB-44us4nhR5wL_tg57K-TblD8Eg')

@bot.message_handler(commands = ['start'])
def welcome(message):
    bot.reply_to(message, 'Привет!')

@bot.message_handler(commands = ['name'])
def welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands = ['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands = ['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands = ['password'])
def generate_text(message):
    bot.reply_to(message, generate(10))

@bot.message_handler(commands = ['flip'])
def flip_coin(message):
    bot.reply_to(message, flip())

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
@bot.message_handler(commands=['bestPhrases'])
def best_phrases(message):
    bot.reply_to(message, phrases())

@bot.message_handler(commands=['username'])
def best_phrases(message):
    bot.reply_to(message, f'Ваш никнейм: {message.from_user.username}')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, '1. Для того, чтобы бот подбросил монету, введите команду "flip"\n'
                          '2. Для того, чтобы бот сгенерировал пароль, введите команду "password"\n'
                          '3. Для того, чтобы бот сгенерировал вам афоризм введите команду "bestPhrases"\n'
                          '4. Для того, чтобы бот с вами поздоровался введите команду "hello"\n'
                          '5. Для того, чтобы узнать имя бота введите команду "name"\n'
                          '6. Для того, чтобы узнать свой никнейм введите команду "username"')

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)




bot.polling()
