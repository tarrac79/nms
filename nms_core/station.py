#!/bin/python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, asdict
from typing import Any, List, Generic, Optional, Union

from typing import List
from .models import Station #, DictStation
from .api import Api
from .api_models import RequestBody

class StationController(Api):
    '''
    Класс для получения станций из системы NMS
    select - выбрать 1 станцию по id
    search - выбрать список станция по условиям
    '''

    def select(self, id: int) -> Station:
        '''
        Запрос на информацию об одной станции.
        Выполнение запроса типа select
        :param id: id станции
        :return: объекс класса Station с информацией пр станции
        '''

        return self._select(Station, id)

    def search(self, **kwargs) -> List[Station]:
        '''
        Запрос на информацию о нескольких станциий по условиям в словаре kwargs.
        Выполнение запроса типа search
        :param kwargs:
        :return: список станций
        '''
        return self._search(Station, self._filter_params(kwargs))

if __name__ == "__main__":
    pass