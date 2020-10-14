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
from sys import argv

from nms_core.preparce_policy_rule import pre_policy, ProtocolType
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
logger.setLevel("INFO")


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

        route_addr = argv[1]
        # route_addr = '10.241.226.1'
        id_station = route.search(addr=route_addr)[0].remote_id
        polycy_station = route.search(remote_id=id_station, addr='0.0.0.0')[0].policy_id

        keys_check = ['invert', 'flag', 'from_', 'to', 'flag_invert', 'equal', 'protocol_type',
                      'ip_address', 'mask', 'flag_last_check']
        keys_actions = [ 'set_tos', 'set_dscp', 'enc_num', 'ts_queue', 'ts_stream', 'acm_channel',
                        'goto_policy', 'call_policy', 'flag_last_action']
        for i in sorted(policy_rule.search(policy_id=polycy_station), key=lambda x:x.order_num):
            i = pre_policy(i)

            if i.action == 'CHECK':

                # if i.check_type == 'CHT_PROTOCOL':
                #     print(i.to_dict())
                # continue
                name = i.check_type
                post_name = ' '.join(map(str.capitalize, name.split('_')[1:]))
                inv = "not " if i.flag == '8192' else ''
                if name in ['CHT_802_1Q_PRIORITY', 'CHT_ICMP_TYPE']:
                    print(f'{i.action}: {post_name} is {inv}equal to {i.value1} ' )
                if name in [ 'CHT_PROTOCOL']:
                    print(f'{i.action}: {post_name} is {inv}equal to {ProtocolType(i.protocol_type).name} ')
                if name in ['CHT_VLAN_NUMBER', 'CHT_TOS', 'CHT_DSCP',]:
                    print(f'{i.action}: {post_name} is from {inv}{i.value1} to {i.value2} ')
                if name in ['CHT_SOURCE_IP_NETWORK', 'CHT_DESTINATION_IP_NETWORK']:
                    print(f'{i.action}: {post_name} is {inv}{i.value1}/{i.value2} ')
                if name in [ 'CHT_SOURCE_TCP_PORT', 'CHT_DESTINATION_TCP_PORT', 'CHT_SOURCE_UDP_PORT', 'CHT_DESTINATION_UDP_PORT']:
                    print(f'{i.action}: {post_name} port is {inv}{i.value1} to {i.value2}')
            else:
                name = i.action_type
                post_name = ' '.join(map(str.capitalize, name.split('_')[1:]))
                end = ' and end potisy' if i.flag_last_action == 1 else ''
                print(f'-> {i.action}: {post_name} = {i.ts_queue} {end}')
                # print(i.to_string())




    except ApiError as e:
        print(e.message)


if __name__ == '__main__':
    main()
