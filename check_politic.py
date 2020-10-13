#!/bin/python3
# -*- coding: utf-8 -*-

import logging.config
from settings import logger_config
from json import load as load_config
from sys import argv

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
logger.setLevel("INFO")

def main():
    # Получение данных для соединения с NMS url, login, password
    # из файла config.cfgкуцйwqrewq
    with open("config.cfg", "r") as write_file:
        config = load_config(write_file)
    # объект station


    route = RouteController(base_url=config["url"], login=config["login"], password=config["password"])
    policy_rule = PolicyRuleController(base_url=config["url"], login=config["login"], password=config["password"])
    try:

        route_addr = argv[1]
        id_station = route.search(addr=route_addr)[0].remote_id
        polycy_station = route.search(remote_id=id_station, addr='0.0.0.0')[0].policy_id

        for i in policy_rule.search(policy_id=polycy_station):
            print(pre_policy(i).to_dict())

    except ApiError as e:
        print( e.message)



if __name__ == '__main__':

    main()





