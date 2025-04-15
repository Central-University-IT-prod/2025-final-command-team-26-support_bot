import re

from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from films_bot.config import app_config
from films_bot.bot.keyboards.main import cancel_kb, main_kb
from films_bot.bot.states.main import Question
from films_bot.db.models import SupportMessage

router = Router()


@router.message(F.chat.func(lambda chat: chat.id == app_config.support_chat_id))
async def answer(message: Message, bot: Bot):
    reply_message = message.reply_to_message
    if reply_message and reply_message.bot == bot:
        support_message_id = re.findall(r'№\d+', reply_message.text)
        if not support_message_id:
            return
        support_message = await SupportMessage.get_or_none(
            id=str(support_message_id[0]).replace('№', '')
        )
        if not support_message:
            await message.answer(
                'Данного обращения не существует или на него уже был дан ответ'
            )
            return
        await bot.send_message(
            chat_id=support_message.chat_id,
            text=f'Ответ на ваше обращение №{support_message.id}:\n{message.text}',
        )
        await support_message.delete()


@router.message(F.text == 'Задать вопрос')
async def ask_question(message: Message, state: FSMContext) -> None:
    await state.set_state(Question.question)
    await message.answer('Отправьте ваш вопрос', reply_markup=cancel_kb)


@router.message(F.text == 'Отменить')
async def cancel_question(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer('Успешно отменено', reply_markup=main_kb)


@router.message(F.text, StateFilter(Question))
async def question(message: Message, bot: Bot):
    support_message = await SupportMessage.create(chat_id=message.chat.id)
    text = f'Обращение №{support_message.id}\n{message.text}'
    await bot.send_message(chat_id=app_config.support_chat_id, text=text)
    await message.answer(
        text=f'Ваше обращение №{support_message.id} зарегистрировано:\n{message.text}',
        reply_markup=main_kb,
    )
