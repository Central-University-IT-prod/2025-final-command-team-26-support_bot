from films_bot.config import app_config

from aiogram import Bot, Dispatcher

bot = Bot(token=app_config.telegram_token)

dp = Dispatcher()