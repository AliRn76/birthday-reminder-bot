import time
from threading import Thread

import pytz
import schedule
from telegram import Update
from telegram.constants import ChatType
from telegram.ext import Application, CommandHandler, ContextTypes

from configs import ADMINS_USER_ID, BOT_TOKEN
from utils import find_birthdays, find_anniversaries, send_birthday_messages, send_anniversary_messages


def run_scheduler():
    schedule.every().day.at('08:00:00', tz=pytz.timezone('Asia/Tehran')).do(scheduler)

    while True:
        schedule.run_pending()
        time.sleep(1)


def scheduler():
    for name in find_birthdays():
        send_birthday_messages(name=name)

    for name in find_anniversaries():
        send_anniversary_messages(name=name)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == ChatType.PRIVATE:
        if str(update.message.from_user.id) in ADMINS_USER_ID:
            return await update.message.reply_text('Hello Sepideh :)')
    await update.message.reply_text('Only Sepideh have access to work with me :(')


def run_bot() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler(["start"], start))
    application.run_polling()


if __name__ == '__main__':
    Thread(target=run_scheduler).start()
    run_bot()
