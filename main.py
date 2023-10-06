import asyncio

from telegram import Telegram
from timetable.service import TimeTableService


if __name__ == "__main__":
    asyncio.run(Telegram.start())
