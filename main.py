import config
import logging
from keyboard import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command, Text
from aiogram import Bot, Dispatcher, executor, types
import psycopg2
from config import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

civil = [
    "Германия",
    "Великое княжество Литовское",
    "Монголы",
    "Испания",
    "Индейцы",
    "Византия",
    "Османская империя",
    "Греция",
    "Аравия",
    "Викинги",
    "Франция",
    "Британия",
    "Япония",
    "Китай",
    "Рим",
    "Русь"
]

lib = {}

connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

connection.autocommit = True

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    with connection.cursor() as cursor:
        postgres_insert_query =""" INSERT INTO users (user_id, user_name, user_surname, username)
                                           VALUES (%s,%s,%s,%s)"""
        record_to_insert = (user_id, user_name, user_surname, username)
        cursor.execute(postgres_insert_query, record_to_insert)


@dp.message_handler(commands=["start"])
async def choose_civil(message: types.Message):
    await message.answer("Выбери цивилизацию:", reply_markup=civilizations)
    await message.answer("Тут будет описание цивилизаций")


@dp.message_handler(commands=["do"])
async def do(message: types.Message):
    await message.answer("Ваши действия", reply_markup=panel)

@dp.message_handler()
async def c(message: types.Message):
    await message.answer("OK", reply_markup=ReplyKeyboardRemove())

    if message.text in civil:
        user_id       = message.from_user.id
        user_name     = message.from_user.first_name
        user_surname  = message.from_user.last_name
        username      = message.from_user.username

        db_table_val(user_id=user_id, user_name=user_name, user_surname=user_surname, username=username)
        await bot.send_message(-703593824, f"{user_id}, {user_name}, {user_surname}, {username}")
        lib[str(user_id)] = []

    if message.text == "Тренировка войск":
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
