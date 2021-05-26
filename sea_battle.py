# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция для запуска команд
def main():
    mybot = Updater("1503131530:AAGemL9jBt4W7tolDajMojeqOV-ftYZyUt0", use_context = True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", rules_of_the_game))

def greet_user(update, context):
    print('Вызвана команда /start')
    update.message.reply_text('Добро пожаловать юный адмирал! Грядет великое сражение, готовы ли вы противостоять врагу и возвеличить ваше имя на все необъятный океан, так назовите же ваше имя адмирал ')
    update.message.reply_text('Если вы готовы к игре назовите ваше имя, если же хотите ознакомиться с правилами вызовите команду "/help"')


# Функция для вывода правил игры
def rules_of_the_game(update, context):
    print("Вызов команды /help")
    update.message.reply_text('Правила "Морского Боя": «Морской бой» — игра для двух участников, в которой игроки по очереди называют координаты на неизвестной им карте соперника. Если у соперника по этим координатам имеется корабль (координаты заняты), то корабль или его часть «топится», а попавший получает право сделать ещё один ход. Цель игрока — первым потопить все корабли противника') # Ввести правила игры!!!!

main()