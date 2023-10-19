import time
from threading import Thread

import pytz
import schedule
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from configs import BOT_TOKEN, FILE_NAME
from utils import find_birthdays, find_anniversaries, send_birthday_messages, send_anniversary_messages, authorization


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
    if await authorization(update):
        await update.message.reply_text('Hello Sepideh :)')
    else:
        await update.message.reply_text('Only Sepideh have access to work with me :(')


async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if await authorization(update):
        if (
                update.message.document.file_name.endswith('.xlsx')
                and update.message.document.mime_type.startswith('application/')
        ):
            new_file = await update.message.effective_attachment.get_file()
            await new_file.download_to_drive(FILE_NAME)
            await context.bot.send_message(
                reply_to_message_id=update.message.id,
                text='Updated Successfully',
                chat_id=update.message.chat_id,
            )
        else:
            await context.bot.send_message(
                reply_to_message_id=update.message.id,
                text='File Format Is Not Valid.',
                chat_id=update.message.chat_id,
            )
    else:
        await update.message.reply_text('Only Sepideh have access to work with me :(')


async def birthday_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Reply to this message your Birthday message')


async def anniversary_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Reply to this message your Anniversary message')


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Reply to this message your Anniversary message')


def run_bot() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler(["start"], start))
    application.add_handler(CommandHandler(["birthday"], birthday_handler))
    application.add_handler(CommandHandler(["anniversary"], anniversary_handler))
    application.add_handler(MessageHandler(filters.Document.ALL, file_handler))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), message_handler))
    application.run_polling()


if __name__ == '__main__':
    Thread(target=run_scheduler).start()
    run_bot()
