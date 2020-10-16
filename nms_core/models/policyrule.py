#!/bin/python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from enum import Enum
from typing import List, Generic, Optional, Union, Any, Iterable

from nms_core.base_api import RT
from nms_core.models.main_class import MainClass

polyrule_format = {

}

class ProtocolType(Enum):
    NONE = 0
    ICMP = 1
    IGMP = 2


class Action(Enum):
    CHECK = 0
    ACTION = 1


class ActionPolitic(Enum):
    ACT_DROP_PACKET = 17
    ACT_SET_QUEUE = 18
    ACT_SET_TS_CHANNEL = 19
    ACT_DISABLE_TCP_ACCEL = 20
    ACT_COMPRESS_RTP_HEADERS = 21
    ACT_DISABLE_SCREENING = 22
    ACT_SET_ACM_CHANNEL = 23
    ACT_DROP_IF_STATION_DOWN = 25
    ACT_ENCRYPT_WITH_KEY = 26
    ACT_SET_TOS = 27
    ACT_SET_DSCP = 28
    ACT_GOTO_POLICY = 29
    ACT_CALL_POLICY = 30
    ACT_COMPRESS_GTP_U = 31


class CheckPolitic(Enum):
    CHT_802_1Q_PRIORITY = 1
    CHT_VLAN_NUMBER = 2
    CHT_TOS = 3
    CHT_DSCP = 4
    CHT_PROTOCOL = 5
    CHT_SOURCE_IP_NETWORK = 6
    CHT_DESTINATION_IP_NETWORK = 7
    CHT_SOURCE_TCP_PORT = 8
    CHT_DESTINATION_TCP_PORT = 9
    CHT_SOURCE_UDP_PORT = 10
    CHT_DESTINATION_UDP_PORT = 11
    CHT_ICMP_TYPE = 12
    CHT_IP_PRECEDENCE_TYPE = 13


@dataclass
class Politic(MainClass):
    id: int
    network_id: int
    hub_network_id: int
    name: str
    type: str
    public: str


@dataclass
class PolicyRule(MainClass):
    order_num: int
    type: int
    policy_id: str
    value1: Union[int, str]
    value2: Union[int, str]


@dataclass
class PolicyRuleCheck(PolicyRule):
    '''
    датакласс политики типа Проверка (Check)
    '''
    check_type: int
    invert: Union[int, str]
    flag: int
    from_: int
    to: int
    flag_invert: int
    equal: int
    protocol_type: int
    ip_address: str
    mask: str
    flag_last_check: int

    def to_str(self):
        pass


@dataclass
class PolicyRuleAction(PolicyRule):
    '''
        датакласс политики типа Действие (Action)
    '''
    action: int
    action_type: int
    ts_queue: int
    ts_stream: int
    enc_num: int
    set_tos: int
    set_dscp: int
    acm_channel: int
    call_policy: int
    goto_policy: int
    flag_last_action: int

    def to_str(self):
        print(self.action_type)


@dataclass
class DictPolicyRule(Generic[RT]):
    item: List[PolicyRuleCheck]


@dataclass
class DictPolicyRuleExtended(Generic[RT]):
    item: List[PolicyRuleAction]


if __name__ == '__main__':
    check = PolicyRuleCheck(order_num=2, type=1, policy_id='426', value1=0, value2='', check_type=1, invert=0, flag=0,
                            from_=0, to=0, flag_invert=0, equal=0, protocol_type=0, ip_address='0.0.0.0', mask='0',
                            flag_last_check=0)

    action = PolicyRuleAction(order_num=15, type=17, policy_id=426, value1='', value2='', action=1, action_type=17,
                              ts_queue=0,
                              ts_stream=0, enc_num=1, set_tos=0, set_dscp=0, acm_channel=0, call_policy=0,
                              goto_policy=0,
                              flag_last_action=1)

    print(action)
