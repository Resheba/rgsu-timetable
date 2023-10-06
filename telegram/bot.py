from aiogram import Bot, Dispatcher

from config import TG_TOKEN
from .router import router


class Telegram:
    _bot: Bot = Bot(token=TG_TOKEN)
    _dp: Dispatcher = Dispatcher()

    @classmethod
    async def start(cls) -> None:
        cls._dp.include_routers(router)
        await cls._dp.start_polling(cls._bot)
