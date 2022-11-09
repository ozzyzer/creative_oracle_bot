from random import choice
import telebot
from telebot import types
import os

bot = telebot.TeleBot('TOKENBOT')
taro = os.listdir('path to jpg files')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Таро")
    btn2 = types.KeyboardButton("Творческий оракул")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}! Выбери, что бы ты хотел сделать: ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Творческий оракул":
        bot.send_message(message.chat.id, text="Этот раздел в разработке!")

    elif message.text == "Таро":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Три карты")
        btn2 = types.KeyboardButton("Крест")
        btn3 = types.KeyboardButton("Пирамида любви")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выбери расклад", reply_markup=markup)

    elif message.text == "Три карты":
        bot.send_message(message.chat.id, text="Ваше прошлое (карта 1), ваше настоящее (карта 2) и ваше будущее (карта 3)")
        new_taro = set()
        while len(new_taro) != 3:
            new_elem = choice(taro)
            new_taro.add(choice(taro))
        card_number = 0
        for i_elem in new_taro:
            card_number += 1
            bot.send_photo(message.chat.id, photo=open(f"path to jpg/{i_elem}", "rb"), caption=f"{str(card_number)} карта")

    elif message.text == "Крест":
        bot.send_message(message.chat.id, text="Смысл проблемы (карта 1), чего не следует делать. (карта 2),что следует сделать (карта 3) и что получится, к чему это приведет (4 карта)")
        new_taro = set()
        while len(new_taro) != 4:
            new_elem = choice(taro)
            new_taro.add(choice(taro))
        card_number = 0
        for i_elem in new_taro:
            card_number += 1
            bot.send_photo(message.chat.id, photo=open(f"path to jpg/{i_elem}", "rb"), caption=f"{str(card_number)} карта")


    elif message.text == "Пирамида любви":
        bot.send_message(message.chat.id,
                         text="Первая позиция - ВЫ: эта карта показывает в каком состоянии находитесь вы в текущей ситуации. То есть только то, что касается вашего внутреннего состояния относительно отношений с партнером \nВторая позиция - ПАРТНЕР: эта карта помогает понять вашего партнера и разобраться как его поведение влияет на вас, как он относятся к вам.\nТретья позиция - ОТНОШЕНИЯ: эта карта говорит о ваших отношениях, которые складываются между вами. И дает возможность вам понять, что происходит между вами и какие стоит сделать выводы.\nЧетвертая позиция - БУДУЩЕЕ: эта карта дает предпосылки для того, чтобы понять какое может быть будущее у вас исходя из вашего текущего поведения, текущего поведения вашего партнера и тех отношений, которые сложились у вас")
        new_taro = set()
        while len(new_taro) != 4:
            new_elem = choice(taro)
            new_taro.add(choice(taro))
        card_number = 0
        for i_elem in new_taro:
            card_number += 1
            bot.send_photo(message.chat.id, photo=open(f"path to jpg/{i_elem}", "rb"), caption=f"{str(card_number)} карта")


    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Таро")
        btn2 = types.KeyboardButton("Творческий оракул")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}! Выбери, что бы ты хотел сделать: ", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Будущее туманно...")

bot.polling(none_stop=True)