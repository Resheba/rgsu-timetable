from dataclasses import dataclass
from bs4 import BeautifulSoup, Tag
from typing import Self

from timetable.request.typpes.response import TimeTableResponse


@dataclass
class Lesson:
    time_from: str = None
    time_to: str = None
    title: str = None
    category: str = None 
    teacher: str = None
    address: str = None
    auditory: str = None

    def __post_init__(self) -> None:
        self.time: str = (self.time_from or '') + ' - ' + (self.time_to or '')



class TimeTable:
    _classes: dict[str, str] = {'time_from': 'n-timetable-day__from', 
                                'time_to': 'n-timetable-day__to', 
                                'title': 'n-timetable-card__title', 
                                'category': 'n-timetable-card__category', 
                                'teacher': 'n-timetable-card__affiliation', 
                                'address': 'n-timetable-card__geo', 
                                'auditory': 'n-timetable-card__auditorium'}

    def __init__(
            self,
            dateName: str= None,
            weekName: str = None,
            weekDay: str = None,
            lessons: tuple[Lesson] = None
    ) -> None:
        self.dateName = dateName
        self.weekName = weekName
        self.weekDay = weekDay
        self.lessons = lessons

    @classmethod
    def parse(
        cls,
        response: TimeTableResponse
    ) -> Self:
        soup: BeautifulSoup = BeautifulSoup(response.html, 'html.parser')
        items: list[Tag] = soup.findAll('div', class_='n-timetable-day__item') or ()
        lessons: list[Lesson] = list()

        for item in items:
            lesson_dict: dict[str, str] = dict()
            for name, class_ in cls._classes.items():
                tag: Tag = item.find(class_=class_)
                if name == 'address':
                    address = ' '.join([
                        geo.getText(strip=True) 
                        for geo in tag.findAll('div') or ()]
                        ).strip()
                    lesson_dict[name] = address
                else:
                    lesson_dict[name] = tag.getText(strip=True) if tag else None
            
            lesson: Lesson = Lesson(**lesson_dict)
            lessons.append(lesson)
        
        return cls(
            dateName=response.dateName,
            weekName=response.weekName,
            weekDay=response.weekDay,
            lessons=tuple(lessons)
        )
    