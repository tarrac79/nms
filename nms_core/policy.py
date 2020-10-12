#!/bin/python3
# -*- coding: utf-8 -*-

from typing import List
from .models import Policy
from .api import Api

class PolicyController(Api):
    '''
    Класс для запросов роутов
    '''

    def select(self, id: int) -> Policy:
        '''
        Запрос на информацию об одной станции.
        Выполнение запроса типа select
        :param id: id станции
        :return: объекс класса Station с информацией пр станции
        '''

        return self._select(Policy, id)

    def search(self, **kwargs) -> List[Policy]:
        '''
        Запрос на информацию о нескольких станциий по условиям в словаре kwargs.
        Выполнение запроса типа search
        :param kwargs:
        :return: список станций
        '''
        return self._search(Policy, self._filter_params(kwargs))