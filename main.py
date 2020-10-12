#!/bin/python3
# -*- coding: utf-8 -*-

import logging.config
from settings import logger_config
from json import load as load_config
from json import dumps

# Импортируем необходжимые классы
from nms_core.station import StationController      # для работы со станциями
from nms_core.route import RouteController      # для работы со станциями
from nms_core.policy import PolicyController      # для работы со станциями
from nms_core.polyrule import PolicyRuleController

from nms_core.preparce_policy_rule import pre_policy

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
# logger.setLevel("DEBUG")


def main():
    # Получение данных для соединения с NMS url, login, password
    # из файла config.cfgкуцйwqrewq
    with open("config.cfg", "r") as write_file:
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

        for i in policy_rule.search(policy_id=polycy_station):
            print(pre_policy(i))

        # print(policy_rule.search(id=37699))
        # for i in policy_rule.search(policy_id=27):
        #     print(i)

        # for i in range(37699, 37710):
        #     try:
        #         print(policy_rule.select(i))  # test select
        #     except Exception:
        #         continue

        # print(policy_rule.select(37258))  # test select

        # print(route.select(22752))






    except ApiError as e:
        print( e.message)



if __name__ == '__main__':
    main()





