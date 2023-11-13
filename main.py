from telebot import types
import telebot

token = "6414242162:AAGYA86EE06F6LQWY88ae-DiwrCHunOk8Mg"
my_chat_id = 1018683356
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Кофе")
    button2 = types.KeyboardButton(text="Чай")
    button3 = types.KeyboardButton(text="Какао")
    button4 = types.KeyboardButton(text="Разное")
    button5 = types.KeyboardButton(text="Личный кабинет")
    button6 = types.KeyboardButton(text="Помощь")
    keyboard.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, "Вас приветствует магазин AllCoffee", reply_markup=keyboard)

def send_request(message):
    mes = f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо за ваш заказ! Наши специалисты скоро свяжутся с вами!')

def send_item_arabica(message):
    bot.send_message(message.chat.id, 'Лот 1001. Бразилия Альта-Виста 1кг - 2400р.')
    bot.send_message(message.chat.id, 'Лот 1002. Бразилия Серрадо - 1кг - 1900р.')

def send_item_robusta(message):
    bot.send_message(message.chat.id, 'Лот 2001. Бразилия Альта-Виста 1кг - 2400р.')
    bot.send_message(message.chat.id, 'Лот 2002. Бразилия Серрадо - 1кг - 1900р.')

def coffee_func(message):
    keyboard = types.ReplyKeyboardMarkup()
    arabica_button = types.KeyboardButton(text='Арабика')
    robusta_button = types.KeyboardButton(text='Робуста')
    keyboard.add(arabica_button, robusta_button)
    bot.send_message(message.chat.id, 'Выберите сорт кофе: Арабика или Робуста', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'кофе':
        coffee_func(message)
    if message.text.lower() == 'арабика':
        bot.send_message(message.chat.id, 'Будем рады Вас обслужить!')
        bot.send_message(message.chat.id, 'Оставьте номер телефона! И номер Лота!')
        bot.register_next_step_handler(message, send_request)
        send_item_arabica(message) 
    if message.text.lower() == 'робуста':
        bot.send_message(message.chat.id, 'Будем рады Вас обслужить!')
        bot.send_message(message.chat.id, 'Оставьте номер телефона! И номер Лота!')
        bot.register_next_step_handler(message, send_request)
        send_item_robusta(message) 
    #bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.infinity_polling()
