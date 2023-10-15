import schedule
from dotenv import dotenv_values

from telegram import Update
from telegram.constants import ChatType
from telegram.ext import Application, CommandHandler, ContextTypes

config = dotenv_values('.env')
BOT_TOKEN = config['BOT_TOKEN']
trusted_ids = config['SEPIDEH_USER_ID'].split(',')


def scheduler():
    context = ...
    send_birthday_messages(context, chat_id=1, name='علی')
    send_yearly_messages(context, chat_id=1, name='علی')


async def send_birthday_messages(context, *, chat_id, name):
    message = '{} جان تولدت مبارک'.format(name)
    await context.bot.send_message(chat_id, text=message)


async def send_yearly_messages(context, *, chat_id, name):
    message = '{} عزیز، سالگرد ورودت به دیجیفای مبارک باشه'.format(name)
    await context.bot.send_message(chat_id, text=message)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == ChatType.PRIVATE:
        if str(update.message.from_user.id) in trusted_ids:
            return await update.message.reply_text('Hello Sepideh :)')
    await update.message.reply_text('Only Sepideh have access to work with me :(')


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler(["start"], start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    schedule.every().day.at('8:00').do(scheduler)
    main()
