from typing import Type, Dict, List, Union, Any

from requests import Session
import logging

from .api_models import RequestBody, Response, Request
from .base_api import BaseApi, RT, ApiError
from .factory import InvalidSerialError, create_factory
from .models import FindParams

# from .models import Station, Traffic, FindParams, DictStation, TrafficExtended, Network, Route
# from .models import PolicyRule, PolicyRuleExtended, Policy, DictPolicy
from .models import Station, Route, Policy, PolicyRuleCheck, PolicyRuleAction


from datetime import datetime

logger = logging.getLogger('nms_logger')




class ResponseError(ApiError):
    pass


class NullDate(ApiError):
    pass


class NMSError(ApiError):
    pass




class Api(BaseApi):
    _logger = logging.getLogger('nms_logger')
    def __init__(self, base_url: str, login: str, password: str, timeout: int = 3):
        super().__init__(base_url, Session(), create_factory(), timeout)
        self.login = login
        self.password = password
        self.types_mapping = {
            Station: "station",
            Route: 'stationroute',
            # DictStation: 'station',
            # Traffic: "traffic",
            # TrafficExtended: "traffic-extended",
            Union[PolicyRuleCheck, PolicyRuleAction]: 'policyrule',
            # PolicyRuleExtended: 'policyrule',
            # PolicyRule: 'policyrule',
            # PolicyRuleExtended: 'policyrule',
            Policy: 'policy',
            # DictPolicy: 'policy'

        }

    def _nms_request(self, body: RequestBody,
                     result_class,
                     data: Type[Union[Any, Dict]] = None):
        '''
        :type: object  тип запроса
        :param body:    запрос
        :param result_class: тип результата
        :return:
        '''

        params = {
            "token": self.password,
            "out": "json",
        }

        response = self._request(method="GET", url="jsonapi",
                                 params=params, body=Request(body, data),
                                 body_class=Request,
                                 result_class=Response[result_class])

        if response and response.result.type == 'success':
            if data is None:
                return response.data
            else:
                return response
        else:
            raise NMSError(errno=response.result['errno'], message=response.result['message'])

    def _list(self, result_class: Type[RT] = Station) -> Type[RT]:
        body = RequestBody(
            action='list',
            object=self.types_mapping[result_class]
        )

        try:

            return self._nms_request(body=body, result_class=result_class).item

        except InvalidSerialError as e:
            raise ApiError from e

    # def station_trafic(self, id: str, start: datetime, stop: datetime,
    #            result_class: Type[RT] = Traffic) -> Type[RT]:
    #
    #     pass

    # def _vno_trafic(self, id: str, start: int, stop: int,
    #                 result_class: Type[RT] = Traffic) -> Type[RT]:
    #
    #     body = RequestBody(
    #         id=id,
    #         action='traffic',
    #         object='network',
    #         from_=start,
    #         to_=stop
    #     )
    #     # print('body: ', body)
    #     return self._nms_request(body=body, result_class=result_class)
    #
    # def _trafic_extended(self, id: str, start: datetime, stop: datetime,
    #                      result_class: Type[RT] = TrafficExtended) -> Type[RT]:
    #     body = RequestBody(
    #         id=id,
    #         action='trafic-extended',
    #         object=self.types_mapping[result_class],
    #         from_=int(start.timestamp()),
    #         to_=int(stop.timestamp())
    #     )
    #     return self._nms_request(body=body, result_class=result_class)

    def _select(self, object_class: Type[RT], id_):
        ''' Запрос типа select к системе NMS

        :param object_class: тип объекта
        :param id: id объекта
        :return: j,]trb
        '''

        body = RequestBody(
            id=id_,
            action='select',
            object=self.types_mapping[object_class]
        )

        return self._nms_request(body=body, result_class=object_class)

    def _search(self, object_class: Type[RT], params: Dict) -> List[RT]:

        # print(object_class)
        body = RequestBody(
            action='search',
            find=FindParams(object=self.types_mapping[object_class], where=params)
        )

        return self._nms_request(body=body, result_class=List[object_class])

    def _update(self, id, object_class: Type[RT], **kwargs):
        '''
        :param id:
        :param object_class:
        :param kwargs:
        :return:
        '''
        try:
            body = RequestBody(
                object=self.types_mapping[object_class],
                action='update',
                id=id)

            return self._nms_request(body=body, result_class=Request, data=kwargs)

        except AttributeError as e:

            logging.error('Api._update', e.args)


if __name__ == '__main__':
    pass

