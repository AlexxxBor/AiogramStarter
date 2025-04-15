import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать!")


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Пока что этот бот не умеет ничего!')


@dp.message(F.text == "Привет!")
async def hello(message: Message):
    await message.reply('Как дела?')


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv('TG_TOKEN'))
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    print('Starting up...')


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
