import logging

from typing import Union, List

from .models import PolicyRuleCheck, PolicyRuleAction
from .api import Api
# from .api_models import RequestBody

class PolicyRuleController(Api):
    def select(self, id: int) -> Union[PolicyRuleCheck, PolicyRuleAction]:
        '''
        Запрос на информацию об одной станции.
        Выполнение запроса типа select
        :param id: id станции
        :return: объекс класса Station с информацией пр станции
        '''

        return self._select(Union[PolicyRuleCheck, PolicyRuleAction] , id)


    def search(self, **kwargs) -> Union[PolicyRuleCheck, PolicyRuleAction]:
        '''
        Запрос на информацию о нескольких станциий по условиям в словаре kwargs.
        Выполнение запроса типа search
        :param kwargs:
        :return: список станций
        '''
        new_search = {}
        # for i in self._search(Union[PolicyRuleCheck, PolicyRuleAction], self._filter_params(kwargs)):
        #     for k, v in i.items():
        #         print(k,v)
        return self._search(Union[PolicyRuleCheck, PolicyRuleAction], self._filter_params(kwargs))