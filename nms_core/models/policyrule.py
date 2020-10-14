#!/bin/python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from enum import Enum

from typing import List, Generic, Optional, Union, Any

from nms_core.base_api import RT
from nms_core.models.main_class import MainClass

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
    id: int
    policy_id: str
    value1: Union[str, int]
    value2: Union[str, int]

@dataclass
class PolicyRuleCheck(PolicyRule):
    invert: str
    flag: str
    from_: str
    to: str
    flag_invert: str
    equal: str


    ip_address: str
    mask: str
    check_type: Optional[str]
    action: Optional[str]
    action_type: Optional[str]
    ts_queue: int
    action_type: str
    flag_last_action: int
    flag_last_check: int

    acm_channel: int
    ts_stream: int
    protocol_type: int
    enc_num: Optional[str] = ''
    set_tos: Optional[str] = ''
    set_dscp: Optional[str] = ''
    call_policy: Optional[int] = 0
    goto_policy: Optional[int] = 0
@dataclass
class PolicyRuleAction(PolicyRuleCheck):
    start_num_mask: Optional[str] = ''
    end: Optional[str] = ''
    addr: Optional[str] = ''









@dataclass
class DictPolicyRule(Generic[RT]):
    item: List[PolicyRuleCheck]


@dataclass
class DictPolicyRuleExtended(Generic[RT]):
    item: List[PolicyRuleAction]
