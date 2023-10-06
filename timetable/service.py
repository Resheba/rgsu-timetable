from .parser.html import TimeTable
from .request.api import TimeTableAPI, TimeTableResponse, GroupQueryResponse

from functools import lru_cache


class TimeTableService:
    @lru_cache
    @staticmethod
    def get_timetable(
        date: str,
        group: str
    ) -> TimeTable | None:
        response: TimeTableResponse = TimeTableAPI.get_timetable(date=date, group=group)
        if response:
           timetable: TimeTable = TimeTable.parse(response=response)
           return timetable
    
    @lru_cache
    @staticmethod
    def get_group(
        group_query: str
    ) -> tuple[str] | None:
        response: GroupQueryResponse = TimeTableAPI.get_group(group_query=group_query)
        if response:
            return response.suggestions
        