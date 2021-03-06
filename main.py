#!/bin/python3
# -*- coding: utf-8 -*-

import logging.config
from settings import logger_config
from json import load as load_config
from json import dumps
from sys import argv

# Импортируем необходжимые классы
from nms_core.station import StationController  # для работы со станциями
from nms_core.route import RouteController  # для работы со станциями
from nms_core.policy import PolicyController  # для работы со станциями
from nms_core.polyrule import PolicyRuleController
from nms_core.models.policyrule import ActionPolitic, CheckPolitic, PolicyRuleCheck

# from nms_core.preparce_policy_rule import pre_policy, ProtocolType
from os import path

from nms_core.api import ApiError

# Настройка логеров
logging.config.dictConfig(logger_config)
logger = logging.getLogger('nms_logger')
# logger.setLevel("DEBUG")
logger.setLevel("INFO")

# CRITICAL 	50
# ERROR		40
# WARNING		30
# INFO		20
# DEBUG		10
# NOTSET		0
# logger.setLevel("INFO")
# logger.setLevel("INFO")


def main():
    # Получение данных для соединения с NMS url, login, password
    # из файла config.cfgкуцйwqrewq

    with open(path.join(path.dirname(__file__), "config.py"), "r") as write_file:
        config = load_config(write_file)
    # объект station
    station = StationController(base_url=config["url"], login=config["login"], password=config["password"])
    route = RouteController(base_url=config["url"], login=config["login"], password=config["password"])
    policy = PolicyController(base_url=config["url"], login=config["login"], password=config["password"])
    policy_rule = PolicyRuleController(base_url=config["url"], login=config["login"], password=config["password"])
    try:

        route_addr = '172.18.200.89'
        id_station = route.search(addr=route_addr)[0].remote_id
        polycy_station = route.search(remote_id=id_station, addr='0.0.0.0')[0].policy_id

        next_action = False
        for poly in sorted(policy_rule.search(policy_id=polycy_station), key=lambda x:x.order_num):
            if poly.type == 1:
                print(poly)
                exit()
            continue

    except ApiError as e:
        print(e.message)


if __name__ == '__main__':
    main()
