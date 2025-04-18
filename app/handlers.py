import asyncio
import random

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject, Command
from aiogram.enums import ChatAction

router = Router()


@router.message(CommandStart(deep_link=True, magic=F.args.isalpha()))
async def cmd_start_referal(message: Message, command: CommandObject):
    await message.answer(f"Привет! Ты пришёл от {command.args}")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(2.0)
    await message.answer("Добро пожаловать!")


@router.message()
async def sanyouchik_buller(message: Message):
    bulling = ['Ляя... Сашка 😘', 'Саня! Бу! 😜', '🙃🙂🙃🙂', 'Это Саша! Спасайтесь! 😱']

    if message.from_user.username == 'Strannik_next':
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=random.choice(bulling))


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Пока что этот бот не умеет ничего!')


@router.message(F.text == "Привет!")
async def hello(message: Message):
    await message.reply('Как дела?')


@router.message(F.text.lower().startswith('прив'))
async def any_greetings(message: Message):
    await message.reply('Здравствуй-здравствуй!')


@router.message(F.photo)
async def handle_photo(message: Message):
    await message.answer('Секундочку...')
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(2)
    file_id = message.photo[-1].file_id
    await message.answer_photo(file_id, caption='Вот твоё фото')


@router.message(F.video)
async def handle_video(message: Message):
    file_id = message.video.file_id
    await message.answer_video(file_id, caption='hello')


@router.message(F.voice)
async def handle_voice(message: Message):
    file_id = message.voice.file_id
    await message.answer_voice(file_id, caption="Кто сказал: ... ?")


@router.message(F.sticker)
async def handle_sticker(message: Message):
    file_id = message.sticker.file_id
    await message.answer_sticker(file_id)


@router.message(Command('get'))
async def cmd_get(message: Message, command: CommandObject):
    await message.reply(f'Вы ввели команду get с параметром {command.args}')


@router.message(Command('get_few'))
async def cmd_get_few(message: Message, command: CommandObject):
    if not command.args:
        await message.answer('Аргументы не переданы')
        return
    try:
        v1, v2 = command.args.split(' ', maxsplit=1)
        await message.reply(f'Вы ввели команду get с параметрами {v1} и {v2}')
    except:
        await message.answer('Введены неверные аргументы')


@router.message(F.text == 'Проверка роутера')
async def check_router(message: Message):
    await message.answer('OK!')
