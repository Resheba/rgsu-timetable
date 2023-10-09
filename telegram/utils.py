from timetable.parser.html import Lesson

from prettytable import PrettyTable, MSWORD_FRIENDLY
from aiogram.types import InlineKeyboardButton


def group_message_formater(
        group: str,
        dateName: str= None,
        weekName: str = None,
        weekDay: str = None,
        lessons: tuple[Lesson] = None
) -> str:
    table: PrettyTable = PrettyTable(('Время', 'Дисц.', 'Препод.', 'Адрес', 'Ауд.'))
    sep: int = 8

    date: str = f"{dateName}  {weekDay}  {weekName}\n{group}\n\n"
    table.add_rows([(lesson.time, lesson.title[:sep], lesson.teacher[:sep], lesson.address[:sep], lesson.auditory) 
                    for lesson in lessons])
    # table.set_style(MSWORD_FRIENDLY)
    return date + table.get_string()


def group_keyboard_formater(
        lessons: tuple[Lesson] = None 
) -> list[list[InlineKeyboardButton]]:
    header: list[InlineKeyboardButton] = [InlineKeyboardButton(text=head, callback_data=head) for head in ('Время', 'Дисциплина', 'Препод.', 'Адрес', 'Аудитория')]
    data: list[list[InlineKeyboardButton]] =[
        [
            InlineKeyboardButton(text=col, callback_data='sosat') for col in (lesson.time, lesson.title, lesson.teacher, lesson.address, lesson.auditory)
        ]
        for lesson in lessons
    ]
    data.insert(0, header)
    return data
