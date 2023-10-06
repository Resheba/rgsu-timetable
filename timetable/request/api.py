from requests import post, Response
from requests_toolbelt.multipart.encoder import MultipartEncoder
from typing import Literal

from .typpes.response import GroupQueryResponse, TimeTableResponse


class TimeTableAPI:
    _url: str ='https://rgsu.net/for-students/timetable/timetable/novyy-format-den-json.html'
    _params_tt: dict[str, str] = {'filial': 'ВУЗ', 'isNaked': '1'}
    _params_gp: dict[str, str] = {'mode': 'group', 'filial': 'ВУЗ'}
    _boundary: str = 'arsch'
    _content_type: str = f'multipart/form-data; boundary={_boundary}'

    @classmethod
    def get_timetable(
        cls,
        date: str,
        group: str
    ) -> TimeTableResponse | None:
        try:
            response: Response = post(
                url=cls._url,
                **cls._get_params(date=date, group=group)
            )
            if response.status_code == 200:
                tt_response: TimeTableResponse = TimeTableResponse(**response.json())
                return tt_response
            
        except Exception as ex:
            print('API get_timetabel', ex)

    @classmethod
    def get_group(
        cls,
        group_query: str
    ) -> GroupQueryResponse | None:
        try:
            response: Response = post(
                url=cls._url,
                params=cls._params_gp,
                data=dict(group=group_query)
            )
            if response.status_code == 200:
                gp_response: GroupQueryResponse = GroupQueryResponse(**response.json())
                return gp_response

        except Exception as ex:
            print('API get_group', ex)

    @classmethod
    def _get_params(
        cls,
        date: str,
        group: str
    ) -> dict[Literal['params', 'headers', 'data'], str | dict]:
        return {
            'params': cls._params_tt,
            'headers': {'Content-Type': cls._content_type},
            'data': MultipartEncoder(
                fields=dict(
                    group=group,
                    date=date
                ),
                boundary=cls._boundary
            )
            }
    