from dataclasses import dataclass

from typing import List, Generic, Optional


from nms_core.base_api import RT
from nms_core.models.main_class import MainClass

@dataclass
class Route(MainClass):
    typename: str
    addr: str
    mask: int
    local_vlan: int
    hub_vlan: int
    local_access: int
    remote_id: int
    controller_id: int
    id: int
    # remote_id: int
    # priority: Optional[int]
    policy_id: int
    shaper_id: Optional[int]
    private: int
    hub_network_id: int
    source_vlan_number: int
    dest_vlan_number: int
    svlan_number: int
    dest_vlan: int
    source_vlan: int
    acl: List = list

@dataclass
class DictRoute(Generic[RT]):
    item: List[Route]