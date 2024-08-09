from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!")

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("Хелп")

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer("fine")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

@router.message(Command("photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAANEZrYo3ldx7S-n6wdDBVNBmbs-fPEAAn7cMRvRiWhJMTgnNj9olwQBAAMCAAN5AAM1B")