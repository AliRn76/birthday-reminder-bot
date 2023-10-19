import asyncio
from datetime import datetime

import schedule
from dotenv import dotenv_values

from telegram import Update
from telegram.constants import ChatType
from telegram.ext import Application, CommandHandler, ContextTypes

config = dotenv_values('.env')
BOT_TOKEN = config['BOT_TOKEN']
trusted_ids = config['SEPIDEH_USER_ID'].split(',')


BIRTHDAY_MESSAGE = '{} جان تولدت مبارک'
YEARLY_MESSAGE = '{} عزیز، سالگرد ورودت به دیجیفای مبارک باشه'


async def scheduler():
    context = ...
    await context.bot.send_message(chat_id, text=BIRTHDAY_MESSAGE.format(name))

    await context.bot.send_message(chat_id, text=YEARLY_MESSAGE.format(name))


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


def sync_scheduler():
    asyncio.run(scheduler())


if __name__ == '__main__':
    schedule.every().day.at('8:00').do(sync_scheduler)
    main()
