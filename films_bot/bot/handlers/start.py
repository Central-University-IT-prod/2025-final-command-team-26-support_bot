from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

from films_bot.bot.keyboards.main import main_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text='Здравствуйте! Это бот поддержки сервиса "Т.Фильмы". Здесь вы можете задать вопрос, если у вас возникли приблемы при использовании сервиса.',
        reply_markup=main_kb
    )
