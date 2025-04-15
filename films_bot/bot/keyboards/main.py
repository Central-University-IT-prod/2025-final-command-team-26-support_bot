from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Задать вопрос')]],
    resize_keyboard=True,
    selective=True,
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Отменить')]],
    resize_keyboard=True,
    selective=True,
)
