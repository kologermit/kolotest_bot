import telebot
import config
import random

from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    config.players[message.from_user.id] = dict(play_stat=False, wins=0, losses=0, draws=0, cansled=0, count=0, skin=0)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    play = types.KeyboardButton("Играть с ботом")
    static = types.KeyboardButton("Статистика")
 
    markup.add(play)
    markup.add(static)
    bot.send_message(message.chat.id, config.start_message, reply_markup=markup)
 

@bot.message_handler(content_types=['text'])
def start_play(message):
    if message.chat.type == 'private':
        if message.text == '/play' or message.text == 'Играть с ботом':
            config.players[message.from_user.id]["play_stat"] = dict(board=[], move=0)
            end = types.KeyboardButton("Закончить игру")
            start = types.KeyboardButton("/start")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            board = []
            for i in range(0, 10):
            	config.players[message.from_user.id]["play_stat"]["board"] += [str(i)]
            markup.add(
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][1]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][2]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][3]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][4]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][5]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][6]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][7]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][8]),
                types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][9])
            )
            markup.add(start, end)
            bot.send_message(message.chat.id, config.play_message, reply_markup=markup)
        elif (message.text == 'O' or message.text == 'X') and config.players[message.from_user.id]["play_stat"] != False:
            if config.players[message.from_user.id]["play_stat"]["move"] > 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][1]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][2]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][3]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][4]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][5]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][6]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][7]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][8]),
                    types.KeyboardButton(config.players[message.from_user.id]["play_stat"]["board"][9])
                )
                end = types.KeyboardButton("Закончить игру")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                bot.send_message(message.chat.id, config.error_play_button_message, reply_markup=markup)
        elif (message.text == 'Закончить игру' or message.text == '/end') and config.players[message.from_user.id]["play_stat"] != False:
            config.players[message.from_user.id]["cansled"] += 1
            config.players[message.from_user.id]["count"] += 1
            config.players[message.from_user.id]["play_stat"] = False
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            play = types.KeyboardButton("Играть с ботом")
            static = types.KeyboardButton("Статистика")
            markup.add(play)
            markup.add(static)
            bot.send_message(message.chat.id, config.cancel_game_message, reply_markup=markup)
        elif (message.text == 'Статистика'):
            bot.send_message(message.chat.id, config.static_message.format(
            	config.players[message.from_user.id]["count"],
            	config.players[message.from_user.id]["wins"],
            	config.players[message.from_user.id]["losses"],
            	config.players[message.from_user.id]["draws"],
            	config.players[message.from_user.id]["cansled"]
             ))
        else:
            bot.send_message(message.chat.id, config.not_message)


bot.polling(none_stop=True)