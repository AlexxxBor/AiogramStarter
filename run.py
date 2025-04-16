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


@dp.message(F.text.lower().startswith('прив'))
async def any_greetings(message: Message):
    await message.reply('Здравствуй-здравствуй!')


@dp.message(F.photo)
async def handle_photo(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer_photo(file_id, caption='Вот твоё фото')


@dp.message(F.video)
async def handle_video(message: Message):
    file_id = message.video.file_id
    await message.answer_video(file_id, caption='hello')


@dp.message(F.voice)
async def handle_voice(message: Message):
    file_id = message.voice.file_id
    await message.answer_voice(file_id, caption="Кто сказал: ... ?")


@dp.message(F.sticker)
async def handle_sticker(message: Message):
    file_id = message.sticker.file_id
    await message.answer_sticker(file_id)


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
