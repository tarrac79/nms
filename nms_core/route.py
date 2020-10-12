#!/bin/python3
# -*- coding: utf-8 -*-

from typing import List
from .models import Route #, DictStation
from .api import Api

class RouteController(Api):
    '''
    Класс для запросов роутов
    '''

    def select(self, id: int) -> Route:
        '''
        Запрос на информацию об одной станции.
        Выполнение запроса типа select
        :param id: id станции
        :return: объекс класса Station с информацией пр станции
        '''

        return self._select(Route, id)

    def search(self, **kwargs) -> List[Route]:
        '''
        Запрос на информацию о нескольких станциий по условиям в словаре kwargs.
        Выполнение запроса типа search
        :param kwargs:
        :return: список станций
        '''

        return self._search(Route, self._filter_params(kwargs))