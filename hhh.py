import telebot
from telebot import types
from requests import get
from telebot.types import ReplyKeyboardMarkup
bot = telebot.TeleBot('5008383917:AAGW7DDYvpyVuYBPDvwLWbyfOeT9VE0uAsA')
# пишем основые кнопки в меню


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('⏰ Расписание')
    item3 = types.KeyboardButton('💭 Прочее')
    item4 = types.KeyboardButton('👩‍🏫 Найти учителя')
    markup.add(item1, item3, item4)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Как дела?'.format(message.from_user),
                     reply_markup=markup)

# прописываем доп меню


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '⏰ Расписание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Расписание уроков')
            item2 = types.KeyboardButton('Расписание звонков')
            item3 = types.KeyboardButton('Расписание пробных экзаменов (9-11 класс)')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Выберите интересующее вас расписание', reply_markup=markup)
        elif message.text == '💭 Прочее':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Шпаргалки')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        elif message.text == 'Расписание пробных экзаменов (9-11 класс)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пока нет информации', reply_markup=markup)
        elif message.text == '👩‍🏫 Найти учителя':
            bot.send_message(message.chat.id,
                             'Введите фамилию преподавателя(с заглавной буквы) и день.\n\nP.S здесь пока только не все учителя, так как это тестовый режим')
        if message.text == 'Шапкина':
            bot.send_message(message.chat.id, 'Расписания Марии Валентиновны на неделю пока нет')
        if message.text == 'Прокопьева понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Xv1NqjcW/image.png").content)
        if message.text == 'Прокопьева вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/x8Cdgkfc/image.png").content)
        if message.text == 'Прокопьева среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/g0jdC99T/image.png").content)
        if message.text == 'Прокопьева четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/DZbhzqwQ/image.png").content)
        if message.text == 'Прокопьева пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/G3GrwJNd/image.png").content)
        if message.text == 'Прокопьева суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/mgXWNdcN/image.png").content)
        if message.text == 'Моисеенкова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/nhs0gTR1/image.png").content)
        if message.text == 'Моисеенкова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/8cKmnrL3/image.png").content)
        if message.text == 'Моисеенкова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/wBXcYrhD/image.png").content)
        if message.text == 'Моисеенкова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/BvBDVK0g/image.png").content)
        if message.text == 'Моисеенкова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/8cj6cXrK/image.png").content)
        if message.text == 'Моисеенкова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Окунева понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/L6WJCVZR/image.png").content)
        if message.text == 'Окунева вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/RVWFHnpY/image.png").content)
        if message.text == 'Окунева среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/bwbw6fhH/image.png").content)
        if message.text == 'Окунева четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/d0YtpNQM/image.png").content)
        if message.text == 'Окунева пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/L6g9XFnK/image.png").content)
        if message.text == 'Окунева суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
            bot.send_photo(message.chat.id, get("").content)
        if message.text == 'Пухно':
            bot.send_message(message.chat.id, 'Расписания Татьяны Николаевны на неделю пока нет')
        if message.text == 'Дмиртриева понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/jqmTB3v8/image.png").content)
        if message.text == 'Дмитриева вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/cJFyhFrB/image.png").content)
        if message.text == 'Дмитриева среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/sX8Fd1PB/image.png").content)
        if message.text == 'Дмитриева четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/5jdZyGRb/image.png").content)
        if message.text == 'Дмитриева пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/dQk37yxx/image.png").content)
        if message.text == 'Дмитриева суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Баранова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/D0VCPGdc/image.png").content)
        if message.text == 'Баранова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Баранова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/7hxz4Yxk/image.png").content)
        if message.text == 'Баранова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/wjSsvk6F/image.png").content)
        if message.text == 'Баранова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/hjnz8PQd/image.png").content)
        if message.text == 'Баранова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Pf2pZHXC/image.png").content)
        if message.text == 'Полякова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Полякова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/xTtmrF6b/image.png").content)
        if message.text == 'Полякова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/NjnrF2qs/image.png").content)
        if message.text == 'Полякова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/yNS3Z6sF/image.png").content)
        if message.text == 'Полякова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/wMF1p7Qd/image.png").content)
        if message.text == 'Полякова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/rwDKBydv/image.png").content)
        if message.text == 'Музыкантова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Музыкантова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/BQyTzVYQ/image.png").content)
        if message.text == 'Музыкантова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/7Lqft1kZ/image.png").content)
        if message.text == 'Музыкантова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/TPQhzydq/image.png").content)
        if message.text == 'Музыкантова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/500jbxjc/image.png").content)
        if message.text == 'Музыкантова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/D04Z4BqB/image.png").content)
        if message.text == 'Крыжановская понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Kzqf8vNt/image.png").content)
        if message.text == 'Крыжановская вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/B665kf0b/image.png").content)
        if message.text == 'Крыжановская среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/d1xRKNsB/image.png").content)
        if message.text == 'Крыжановская четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/zvHCDw31/image.png").content)
        if message.text == 'Крыжановская пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/44YqHr9X/image.png").content)
        if message.text == 'Крыжановская суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/mZKqY8YC/image.png").content)
        if message.text == 'Филюшкина':
            bot.send_message(message.chat.id, 'Расписание Ольги Вадимовны на неделю пока нет')
        if message.text == 'Дикушин':
            bot.send_message(message.chat.id, 'Расписание Максима Александровича на неделю пока нет')
        if message.text == 'Горяинова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/JzBR3Pdk/2021-12-24-21-37-34.png").content)
        if message.text == 'Горяинова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Горяинова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/HsqqmHBr/2021-12-24-21-39-38.png").content)
        if message.text == 'Горяинова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Sxbv5dx8/2021-12-24-21-40-32.png").content)
        if message.text == 'Горяинова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/KzjqLs0X/2021-12-24-21-41-23.png").content)
        if message.text == 'Горяинова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Pfphn6TF/2021-12-24-21-42-11.png").content)
        if message.text == 'Хамилляйнен понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/1R2gMHFS/image.png").content)
        if message.text == 'Хамилляйнен вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Y9j9zGqj/image.png").content)
        if message.text == 'Хамилляйнен среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/RhHZ2ktB/image.png").content)
        if message.text == 'Хамилляйнен четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Хамилляйнен пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/52qmF0tZ/image.png").content)
        if message.text == 'Хамилляйнен суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/DzpLqb3Y/image.png").content)
        if message.text == 'Абрамова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/1R2gMHFS/image.png").content)
        if message.text == 'Абрамова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Y9j9zGqj/image.png").content)
        if message.text == 'Абрамова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Абрамова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Абрамова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/52qmF0tZ/image.png").content)
        if message.text == 'Абрамова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/DzpLqb3Y/image.png").content)
        if message.text == 'Бякина понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/4y6YFYjG/image.png").content)
        if message.text == 'Бякина вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/SN42YGzx/image.png").content)
        if message.text == 'Бякина среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/MGnvJPgd/image.png").content)
        if message.text == 'Бякина четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/d0gDsRYv/image.png").content)
        if message.text == 'Бякина пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Vsq5wbHQ/image.png").content)
        if message.text == 'Бякина суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Чебан понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/QdHXFBSM/image.png").content)
        if message.text == 'Чебан вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/vBLyJ580/image.png").content)
        if message.text == 'Чебан среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Чебан четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/G2zNPKmn/image.png").content)
        if message.text == 'Чебан пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Чебан суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Лапина понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Лапина вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/1RV73wkt/image.png").content)
        if message.text == 'Лапина среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/RZ4gd8N6/image.png").content)
        if message.text == 'Лапина четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/qMXLNLjk/image.png").content)
        if message.text == 'Лапина пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/zGzkKgcT/image.png").content)
        if message.text == 'Лапина суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/dV5jBVbp/image.png").content)
        if message.text == 'Федюк понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Федюк вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Федюк среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/cHD9tJFs/image.png").content)
        if message.text == 'Федюк четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/XYwscLs1/image.png").content)
        if message.text == 'Федюк пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/B6vN304R/image.png").content)
        if message.text == 'Федюк суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/HWFG6StT/image.png").content)
        if message.text == 'Гутченко':
            bot.send_message(message.chat.id, 'Расписания пока нет')
        if message.text == 'Хлынова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Хлынова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Хлынова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
        if message.text == 'Хлынова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Хлынова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Хлынова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Матвеева понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/c4fzXdHc/image.png").content)
        if message.text == 'Матвеева вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/R0ZbSfTP/image.png").content)
        if message.text == 'Матвеева среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/ZKz79Xcv/image.png").content)
        if message.text == 'Матвеева четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Матвеева пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/RFf14V2s/image.png").content)
        if message.text == 'Матвеева суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/KY1rp5fy/image.png").content)
        if message.text == 'Кшвецкая понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/FRtcWX1j/image.png").content)
        if message.text == 'Кшвецкая вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/RhdHZ3dR/image.png").content)
        if message.text == 'Кшвецкая среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/hP4m3r43/image.png").content)
        if message.text == 'Кшевцкая четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Кшевецкая пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/76yG11Q9/image.png").content)
        if message.text == 'Кшвецкая суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/2yk1MkYB/image.png").content)
        if message.text == 'Посохова':
            bot.send_message(message.chat.id, 'Расписание Елены Валентиновны на неделю пока нет')
        if message.text == 'Ляхова понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Ляхова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/4NZ02n0x/2.png").content)
        if message.text == 'Ляхова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Ляхова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/sgLwz2TS/4.png").content)
        if message.text == 'Ляхова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
            bot.send_photo(message.chat.id, get("").content)
        if message.text == 'Ляхова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/tgVD4Hcc/image.png").content)
        if message.text == 'Стрижак понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/7hr36GzG/image.png").content)
        if message.text == 'Стрижак вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Hn0Q7Y0S/image.png").content)
        if message.text == 'Стрижак среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/ZY6PQHkr/image.png").content)
        if message.text == 'Стрижак четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/QxsgZ7sv/image.png").content)
        if message.text == 'Стрижак пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/T33rpXK9/image.png").content)
        if message.text == 'Стрижак суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/8zXLvnWV/image.png").content)
        if message.text == 'Барабашина понедельник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/fTgCNLLs/image.png").content)
        if message.text == 'Барабашина вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Барабашина среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/hjr834wH/image.png").content)
        if message.text == 'Барабашина четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'https://i.postimg.cc/wxwcXvDN/image.png', reply_markup=markup)
            bot.send_photo(message.chat.id, get("").content)
        if message.text == 'Барабашина пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'https://i.postimg.cc/BQt5M0CV/image.png', reply_markup=markup)
            bot.send_photo(message.chat.id, get("").content)
        if message.text == 'Барабашина суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
        if message.text == 'Полищук':
            bot.send_message(message.chat.id, 'Расписание Василия Владимировича на неделю пока нет')
        if message.text == 'Литвинюк понедльник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Литвинюк вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Литвинюк среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Литвинюк четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Литвинюк пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Литвинюк суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Расписания пока нет', reply_markup=markup)
        if message.text == 'Добронравина понедльник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/BbyX6Rkh/image.png").content)
        if message.text == 'Добронравина вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/7YF5y8gh/image.png").content)
        if message.text == 'Добронравина среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/y80k1QPP/image.png").content)
        if message.text == 'Добронравина четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/D0WwtB01/image.png").content)
        if message.text == 'Добронравина пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/zXKgvGDK/image.png").content)
        if message.text == 'Добронравина суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/DzjWHW5k/image.png").content)
        if message.text == 'Шумеленкова понедльник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/hP7k6HD2/image.png").content)
        if message.text == 'Шумеленкова вторник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Mp2CSdXq/image.png").content)
        if message.text == 'Шумеленкова среда':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/V6VhHF3y/image.png").content)
        if message.text == 'Шумеленкова четверг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/bdXBqwy3/image.png").content)
        if message.text == 'Шумеленкова пятница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/L4q44Q41/image.png").content)
        if message.text == 'Шумеленкова суббота':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Учителя нет в этот день', reply_markup=markup)
# назначение функциями для команды 'назад'

        elif message.text == '🔙 Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('⏰ Расписание')
            item3 = types.KeyboardButton('💭 Прочее')
            item4 = types.KeyboardButton('👩‍🏫 Найти учителя')
            markup.add(item1, item3, item4)
            bot.send_message(message.chat.id, 'Привет, {0.first_name}! Как дела?'.format(message.from_user),
                             reply_markup=markup)

        elif message.text == 'Шпаргалки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Математика')
            item2 = types.KeyboardButton('Физика')
            item3 = types.KeyboardButton('Русский язык')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        elif message.text == 'Физика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Механика')
            item2 = types.KeyboardButton('Электростатика')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        elif message.text == 'Механика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Кинематика')
            item2 = types.KeyboardButton('Динамика')
            item3 = types.KeyboardButton('Статика')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        elif message.text == 'Электростатика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Держи шпору:)', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/vBh0ptk8/2.jpg").content)
        elif message.text == 'Кинематика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Держи шпору:)', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/Y09VfJ83/image.png").content)
        elif message.text == 'Динамика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Держи шпору:)', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/K879TqfH/image.png").content)
        elif message.text == 'Статика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Держи шпору:)', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/j2WgJR3H/image.png").content)
        elif message.text == 'Русский язык':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            item1 = types.KeyboardButton('Огэ/Егэ')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        elif message.text == 'Огэ/Егэ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Держи шпору:)', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/jdp9PJbL/image.jpg").content)
        elif message.text == 'Математика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            item1 = types.KeyboardButton('Огэ')
            item2 = types.KeyboardButton('Егэ')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        elif message.text == 'Огэ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Держи шпору:)')
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/W3NxtLP8/image.jpg").content)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/nr5WdX9S/2.jpg").content)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/qBZWB5Dc/3.jpg").content)
        elif message.text == 'Егэ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Держи шпору:)')
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/85Q2hKrJ/image.jpg").content)
        elif message.text == 'Расписание уроков':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Класс')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        elif message.text == 'Расписание звонков':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/yNPQLn3p/2.jpg").content)
# прописываем выбор класса

        elif message.text == 'Класс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item5 = types.KeyboardButton('8-А')
            item6 = types.KeyboardButton('8-Б')
            item7 = types.KeyboardButton('8-В')
            item8 = types.KeyboardButton('9-А')
            item9 = types.KeyboardButton('9-Б')
            item10 = types.KeyboardButton('9-В')
            item11 = types.KeyboardButton('10-А')
            item12 = types.KeyboardButton('10-Б')
            item13 = types.KeyboardButton('11-А')
            item14 = types.KeyboardButton('11-Б')
            item15 = types.KeyboardButton('11-В')
            back = types.KeyboardButton('🔙 Назад')
            markup.add(item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, back)
            bot.send_message(message.chat.id, 'Выберите класс', reply_markup=markup)

# прописываем отпраку фото расписания для классов

        elif message.text == '8-А':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("").content)
        elif message.text == '8-Б':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/qMB2bC8w/8.png").content)
        elif message.text == '8-В':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/k4dbxVJx/8.png").content)
        elif message.text == '9-А':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/FH8cHWwC/9.png").content)
        elif message.text == '9-Б':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/0jj2mxwY/9.png").content)
        elif message.text == '9-В':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/HLmYzbMs/9.png").content)
        elif message.text == '10-А':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("").content)
        elif message.text == '10-Б':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/636VgHSH/2021-12-24-23-44-03.png").content)
        elif message.text == '11-А':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/ZnW4ncGj/11.png").content)
        elif message.text == '11-Б':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           get("https://i.postimg.cc/sDZ3RT9g/11.png").content)
        elif message.text == '11-В':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('🔙 Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Пожалуйста:', reply_markup=markup)
            bot.send_photo(message.chat.id, get("https://i.postimg.cc/sDHd1qsr/11.png").content)


bot.polling(none_stop=True)
