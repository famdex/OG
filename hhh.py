import telebot
from telebot import types
import random
bot = telebot.TeleBot('')

#пишем основые кнопки в меню
@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('⏰ Расписание')
	item2 = types.KeyboardButton('📖 Информация о боте')
	markup.add(item1, item2)
	bot.send_message(message.chat.id, 'Привет, {0.first_name}! Как дела?'.format(message.from_user), reply_markup=markup)

# прописываем
@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == '⏰ Расписание':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Расписание уроков')
			item2 = types.KeyboardButton('Расписание столовой')
			item3 = types.KeyboardButton('Расписание пробных экзаменов (9-11 класс)')
			back = types.KeyboardButton('🔙 Назад')
			markup.add(item1, item2, item3, back)
			bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)
		elif message.text == '📖 Информация о боте':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			back = types.KeyboardButton('🔙 Назад')
			markup.add(back)
			bot.send_message(message.chat.id, 'Меня создал Ваня Платов', reply_markup=markup)
			bot.send_message(message.chat.id, 'Игра - рандомное число. Кстати, вот твоё число: ' + str(random.randint(1, 10)), reply_markup=markup)
		elif message.text == '🔙 Назад':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('⏰ Расписание')
			item2 = types.KeyboardButton('📖 Информация о боте')
			markup.add(item1, item2)
			bot.send_message(message.chat.id, 'привет,{0.first_name}! Как дела?'.format(message.from_user),
			reply_markup=markup)



		elif message.text == 'Расписание уроков':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Класс')
			back = types.KeyboardButton('🔙 Назад')
			markup.add(item1, back)
			bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)


		elif  message.text == 'Класс':
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
			back = types.KeyboardButton('🔙 Назад')
			markup.add(item5, item6, item7, item8, item9, item10, item11, item12, item13, item14)
			bot.send_message(message.chat.id, 'Выберите класс', reply_markup=markup)
		elif message.text == '8-Б':
			bot.send_message(message.chat.id, '')
		elif message.text == '8-В':
			bot.send_message(message.chat.id, 'что-то')
		elif message.text == '9-А':
			bot.send_message(message.chat.id, 'что-то')
		elif message.text == '9-Б':
			bot.send_message(message.chat.id, 'что-то')
		elif message.text == '9-В':
			bot.send_message(message.chat.id, 'что-то')
		elif message.text == '10-А':
			bot.send_message(message.chat.id, 'что-то')
		elif message.text == '10-Б':
			bot.send_message(message.chat.id, 'что-то')
		elif message.text == '11-А':
			bot.send_message(message.chat.id, 'что-то')
		elif message.text == '11-Б':
			bot.send_message(message.chat.id, 'что-то')
bot.polling(none_stop=True)

