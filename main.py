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

lib = {}



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
    if message.text == "Тренировка войск":
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
