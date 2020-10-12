from dataclasses import dataclass
from nms_core.models.main_class import MainClass
from typing import Generic, List
from nms_core.base_api import RT


# from typing import Union

@dataclass
class Policy(MainClass):
    id: int
    network_id: int
    hub_network_id: int
    name: str
    type: str
    public: int

@dataclass
class DictPolicy(Generic[RT]):
    item:  List[Policy]