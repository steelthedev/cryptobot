import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler , Filters
from tracker import *


telegram_bot_token = "1510402801:AAEN0FMj6w_INdxJnR91Tvq-sD8ItCBFrPA"


updater = Updater(token=telegram_bot_token, use_context=True)


dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id

    data=get_prices()

    messages=""

    for i in data:

        messages += f"Coin: { i['coin']}\nPrice: ${i['price']:,.2f}\nHour Change: {i['change_hour']:.3f}%\nDay Change: {i['change_day']:.3f}%\n\n"


    context.bot.send_message(chat_id=chat_id, text=messages)

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()

updater.idle()