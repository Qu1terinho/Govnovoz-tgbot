from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from random import choice
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    with open('urls.txt', 'r') as file:
        content = (file.read())
    content = content.split(',')
    content = choice(content)
    await message.answer(content)
    file.close()
@start_router.message(F.text == 'еще')
async def cmd_start_2(message: Message):
    with open('urls.txt', 'r') as file:
        content = (file.read())
    content = content.split(',')
    content = choice(content)
    await message.answer(content)
    file.close()
@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Дениска-пиписка')


