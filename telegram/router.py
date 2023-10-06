import logging
from datetime import datetime
from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command, CommandObject

from telegram.utils import group_message_formater, group_keyboard_formater
from timetable import TimeTableService


logging.basicConfig(level=logging.INFO)

router: Router = Router()


@router.inline_query()
async def inline_group_search(query: InlineQuery):
    text: str = query.query or ''
    groups: tuple[str] = TimeTableService.get_group(group_query=text) or ()
    results: list[InlineQueryResultArticle] = [
        InlineQueryResultArticle(
            id=group,
            title=group,
            # description='Description',
            input_message_content=InputTextMessageContent(
                message_text=f'/group {group}',
                parse_mode='HTML'
            )
        ) 
        for group in groups[:20]
    ]

    await query.answer(results=results)


@router.message(Command('group'))
async def get_timetable(message: Message, command: CommandObject):
    group: str = command.args
    if group:
        group: str = group.strip()
        date: str = datetime(year=2023, month=10, day=6).strftime("%Y-%m-%d")
        timetable = TimeTableService.get_timetable(group=group, date=date)
        if timetable:
            text: str = group_message_formater(group=group, dateName=timetable.dateName, weekDay=timetable.weekDay, weekName=timetable.weekName, lessons=timetable.lessons)
            print(text)
            await message.answer(text=text, reply_markup=InlineKeyboardMarkup(inline_keyboard=group_keyboard_formater(timetable.lessons), resize_keyboard=True))
    else:
        await message.answer('/group <код-направления>')
