from datetime import datetime
from typing import Iterator

import jdatetime
import openpyxl


def read_excel() -> Iterator[tuple[str, datetime.date, datetime.date]]:
    dataframe = openpyxl.load_workbook('users.xlsx').active

    for row in range(0, dataframe.max_row):
        first_name, last_name, birthday, anniversary_day = dataframe.iter_cols(1, 4)

        birthday = jdatetime.date(*map(int, birthday[row].value.split('/'))).togregorian()
        anniversary_day = jdatetime.date(*map(int, anniversary_day[row].value.split('/'))).togregorian()
        yield f'{first_name[row].value} {last_name[row].value}', birthday, anniversary_day


def find_birthdays() -> Iterator[str]:
    today = datetime.now()

    for name, birthday, _ in read_excel():
        if today.month == birthday.month and today.day == birthday.day:
            yield name


def find_anniversaries() -> Iterator[str]:
    today = datetime.now()

    for name, _, anniversary in read_excel():
        if today.month == anniversary.month and today.day == anniversary.day:
            yield name
