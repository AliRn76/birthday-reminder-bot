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
