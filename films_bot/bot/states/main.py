from aiogram.fsm.state import State, StatesGroup


class Question(StatesGroup):
    question = State()
