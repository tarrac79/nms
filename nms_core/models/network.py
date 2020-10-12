from dataclasses import dataclass
from nms_core.models.baze_class import BaseClass

@dataclass
class Network(BaseClass):
    id: str
    hub_network_id: str
    name: str


