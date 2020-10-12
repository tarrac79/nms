from datetime import datetime
from typing import Union

from dataclass_factory import Schema, Factory
from dataclass_factory.schema_helpers import type_checker

from .models import Station
# from .models import Traffic
# from .models import TrafficExtended
# from .models import Network
# from .api_models import ResponseResult
from .models import PolicyRuleCheck, PolicyRuleAction


class InvalidSerialError(Exception):
    pass


class DateSchema(Schema[datetime]):
    def parser(self, data: Union[datetime, str, int]):
        try:
            data = int(data)
        except ValueError:
            if isinstance(data, str):
                return datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
        return datetime.fromtimestamp(data)


class StationSchema(Schema):
    def post_parse(self, data: Station):
        if data.serial_num == '00000':
            raise InvalidSerialError
        return data

# class PolyruleSchema(Schema):
#
#     def pre_parse(self, data:dict):
#
#         if int(data['action_type']) == 17:
#             return data
#         raise ValueError

def create_factory():
    return Factory(
        schemas={
            datetime: DateSchema(),
            Station: StationSchema(),
            PolicyRuleCheck: Schema(pre_parse=type_checker("0", field="action")),
            PolicyRuleAction: Schema(pre_parse=type_checker("1", field="action")),
        },
        default_schema=Schema(
            omit_default=True,
        ),
        debug_path=True)


if __name__ == '__mail__':
    pass
