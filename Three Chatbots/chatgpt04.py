# TELEGRAM <<<<<<<<<<<<<3
from telegram.ext import Updater, MessageHandler, Filters
import openai

openai.api_key = "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"
TELEGRAM_API_TOKEN = "6453573891:AAHyHq7I91X3DyndIKAZck1NMsqoc1pjNdM"

def text_message(update, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "system", "content": "Ass a silly phrase after each one of your answers"}]
    )
    update.message.reply_text(response["choices"][0]["message"]["content"])


updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(filters.text & (~filters.command), text_message))
updater.start_polling()
updater.idle()