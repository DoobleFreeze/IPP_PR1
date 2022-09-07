from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Bot, InputMediaPhoto

token_tg = '5575688131:AAFa98mxuAhsj7p4zHJqPwChMqnQpe9PIQg'
bot = Bot(token_tg)
updater = Updater(token_tg, use_context=True)
dp = updater.dispatcher


def start(update, co):
    update.message.reply_text("Введите координаты")


def echo(update, co):
    a = [InputMediaPhoto(f"https://static-maps.yandex.ru/1.x/?ll={update.message.text}&spn=0.006457,0.00619&l=map")]
    bot.send_media_group(chat_id=update.message.from_user.id, media=a)


dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
