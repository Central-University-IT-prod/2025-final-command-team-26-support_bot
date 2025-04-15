import asyncio
import logging

from films_bot.bot import bot, dp
from films_bot.config import app_config
from films_bot.db import init_db
from films_bot.bot.handlers import start, support


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    )

    await init_db(
        username=app_config.postgres_user,
        password=app_config.postgres_password,
        db_name=app_config.postgres_db,
        host=app_config.postgres_host,
    )
    
    dp.include_router(start.router)
    dp.include_router(support.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
