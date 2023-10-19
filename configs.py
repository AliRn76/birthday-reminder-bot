from dotenv import dotenv_values

config = dotenv_values('.env')


BOT_TOKEN = config['BOT_TOKEN']
ADMINS_USER_ID = config['ADMINS_USER_ID'].split(',')
CHAT_ID = config['CHAT_ID']

BIRTHDAY_MESSAGE = (
    '{} جان، همکار عزیز\n'
    ' تولدت، فرصت مناسبی برای یادآوری حضور ارزشمندت برای ما در دیجیفایه!\n'
    ' امیدواریم زندگی با شادی و موفقیت رو تجربه کنی.\n'
    ' تولدت مبارک. 🤍'
)
ANNIVERSARY_MESSAGE = '{} عزیز، امروز سالگرد دیجیفایی شدنته، خوشحالیم که داریمت. 🫶'

MESSAGES = {
    'anniversary': ANNIVERSARY_MESSAGE,
    'birthday': BIRTHDAY_MESSAGE,
}

FILE_NAME = 'users.xlsx'

ANNIVERSARY_MESSAGE_REQUEST = 'لطفا پیام تبریک سالگرد مورد نظر خودتون رو روی همین پیام ریپلای کنید.\nمثال:\n\n{} عزیز، سالگرد دیجیفایی شدنت مبارک.'

BIRTHDAY_MESSAGE_REQUEST = 'لطفا پیام تبریک تولد مورد نظر خودتون رو روی همین پیام ریپلای کنید.\nمثال:\n\n{} عزیز تولدت مبارک.\nامیدوارم سال خوبی پیش رو داشته باشی.'
