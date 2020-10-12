#!/bin/python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, asdict
from typing import Any, List, Generic, Optional, Union

from nms_core.base_api import RT
from nms_core.models.main_class import MainClass


@dataclass
class Station(MainClass):
    name: str
    serial_num: str
    rx_controller: int
    tx_controller: int
    latitude: float
    longitude: float
    tftp_ip: str
    hub_network_id: int
    uhp_model: Union[int, str]
    latitude_deg: int
    latitude_min: int
    longitude_deg: int
    longitude_min: int
    tdma_bw_profile: int = 0
    network_id: int = None
    id: Optional[int] = None
    number: int = 0
    remote_comment: str = ''
    auto_num: str = '1'
    phone1: str = ''
    phone2: str = ''
    enabled: str = '0'
    shaper_id: str = '0'
    dhcp_ip_start: str = '192.168.1.2'
    dhcp_ip_end: str = '192.168.1.254'
    dhcp_mask: str = '24'
    dhcp_gw: str = '192.168.1.1'
    dhcp_dns: str = '192.168.1.1'
    tftp_vlan: int = 0
    dhcp_enable: int = 0
    snmp_ip1: str = '0.0.0.0'
    snmp_ip2: str = '0.0.0.0'
    dhcp_lease: int = 86400
    snmp_write: str = 'private'
    snmp_read: str = 'public'
    icon: Any = ''
    color: Any = ''
    comment: Any = ''
    company: str = ''
    email: str = ''
    address: str = ''
    state_code: int = None




@dataclass
class DictStation(Generic[RT]):
    item:  List[Station]
