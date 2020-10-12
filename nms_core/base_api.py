#!/bin/python3
# -*- coding: utf-8 -*-

from time import sleep
import logging
from json import JSONDecodeError, dumps
from typing import Optional, Dict, Type, Sequence, TypeVar, Any

from dataclass_factory import Factory
from requests import Session, RequestException

RT = TypeVar("RT")
BT = TypeVar("BT")

logger = logging.getLogger('nms_logger')


class ApiError(Exception):
    def __init__(self, errno=0, message='', json=None, answer=None):
        super().__init__()
        self.errno = errno
        self.message = message
        self.json = json
        self.answer = answer



class BaseApi:
    _logger = logging.getLogger('nms_logger')

    def __init__(self, base_url: str, session: Session, factory: Factory, timeout: int = 3):
        ''' Инициализация класса

        :param base_url: url NMS
        :param session: Сессия
        :param factory: библиотека factory
        :param timeout: таймаут подключения
        '''
        self.base_url = base_url  # url
        self.session = session  # Сессия из request
        self.factory = factory
        self.timeout = timeout

    def _filter_params(self, params: Optional[Dict], skip: Sequence = None):
        ''' Убирает из словаря params параметры, которые указали в skip
        так же убирает self

        :param params: исходный словарь
        :param skip: параметры, которые необходимо удалить
        :return: очищенный словарь
        '''
        if not params:
            print(params)
            return params
        return {
            k: v
            for k, v in params.items()
            if v != self or (skip and v in skip)
        }

    def handle_error(self, method: str, status_code: int, response: Any):
        pass

    def _check_error(self, json_answer):

        return json_answer['type'] == 'success'

    def _request(self, *, url: str, method: str,
                 params: Optional[Dict] = None, body: Optional[BT] = None,
                 body_class: Optional[Type[BT]] = None,
                 result_class: Optional[Type[RT]] = None) -> RT:
        '''
        Функция делает запрос типа method на url получает результат список классов,
        :param url: url NMS
        :param method: post/get
        :param params: фильтр
        :param body: запрос
        :param body_class: класс запроса
        :param result_class: класс результата
        :return: список классов result_class
        '''
        if body_class:

            try:
                body = self.factory.dump(body, body_class)
                # TODO: сделать конкретные исключения
            except Exception as e:
                logging.critical(e)
                raise e
        url = "%s/%s/" % (self.base_url, url)

        try:  # Запрос в NMS и проверки корректного ответа
            # self._logger.info(1, result_class, body_class)
            self._logger.info(dumps(body))

            sleep(0.5)
            response = self.session.request(
                method=method,
                url=url,
                params=self._filter_params(params, (result_class, body_class)),
                json=body,
                timeout=self.timeout
            )

            if not response.ok:
                return self.handle_error(method, response.status_code, response)

            result = response.json()

            answer_result = result['result']
            if not self._check_error(answer_result):


                self._logger.debug(dumps(answer_result))

                raise ApiError(errno=answer_result['errno'],
                               message=answer_result['message'],
                               json=body,
                               answer=answer_result)

            if result_class:
                try:
                    # print(result, result_class, sep='\n')
                    return self.factory.load(result, result_class)
                    # parser = self.factory.parser(result_class)
                    # print(parser)
                    # return parser(result)

                except (ValueError, TypeError) as e:
                    raise

        except RequestException as error:

            self._logger.error(
                "RequestException when connecting with url: `%s`, error: `%s`",
                url, error
            )
            raise ApiError("RequestException") from error
        except JSONDecodeError as error:

            self._logger.critical(
                "Cannot decode response for url: `%s`, error: `%s`",
                url, error
            )
            raise ApiError("Cannot decode response") from error

        except Exception as e:
            raise
