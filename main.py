import telebot

mbot = telebot.TeleBot('5891623976:AAEZiDVGgRgtUpj8Ijg-NMfnwt7IX6UvUgE')

@mbot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        mbot.send_message(message.from_user.id, 'What is you name?')
    elif message.text == '/commands':
        mbot.send_message(message.from_user.id, 'helped')
    else:
        mbot.send_message(message.from_user.id, 'okey try')

mbot.polling(none_stop=True, interval=0)
