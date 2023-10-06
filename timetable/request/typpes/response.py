

class TimeTableResponse:
    def __init__(self,
                dateName: str = None,
                html: str = None,
                html2: str = None,
                status: str = None,
                weekDay: str = None,
                weekName: str = None,
                **extra
    ) -> None:
        self.dateName: str = dateName
        self.html: str = html
        self.html2: str = html2
        self.status: str = status
        self.weekDay: str = weekDay
        self.weekName: str = weekName
        self.extra: dict = extra

class GroupQueryResponse:
    def __init__(
            self,
            query: str = None,
            suggestions: list[str] = None,
            **extra
            ) -> None:
        self.query: str = query
        self.suggestions: tuple[str] = tuple(suggestions or ())
        self.extra: dict = extra
