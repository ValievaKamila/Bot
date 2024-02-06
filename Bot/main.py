import telebot
import random
from telebot import types
# Загружаем список предсказаний
f = open('60predictions.txt', 'r', encoding='UTF-8')
prediction = f.read().split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot('6820320249:AAGWqRs2VPdmYkSDicMkLWV0LHa9owqb2Cg')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Получить предсказание")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Нажми \nПОЛУЧИТЬ ПРЕДСКАЗАНИЕ ↓↓↓ \nдля того, чтобы узнать девиз сегодняшнего дня :)',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный предсказание
    if message.text.strip() == 'Получить предсказание' :
            answer = random.choice(prediction)
            mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
            bot.send_message(message.chat.id, f"Привет, {mention}!", parse_mode="HTML")
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)