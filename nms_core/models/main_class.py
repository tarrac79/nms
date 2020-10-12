#!/bin/python3
# -*- coding: utf-8 -*-
from dataclasses import asdict

# Базовый класс, от которого будут наследоваться все классы

class MainClass:
    def to_string(self):
        '''
        Форматирование вывода в удобочитаемом виде
        class (
            elem = value,
            ...
        )
        :return: Отформатированный класс для печати в консоли (для отладки)
        '''
        # список полей и значений через \n
        items_part = "\n".join([f"\t {k}: {v}" for k, v in vars(self).items()])
        string = f"{self.__class__.__name__}(\n{items_part}\n)"
        return string

    def to_dict(self):
        return asdict(self)

