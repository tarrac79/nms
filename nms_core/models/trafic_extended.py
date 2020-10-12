from .traffic import Traffic
from dataclasses import dataclass
from typing import Dict
from datetime import datetime
from nms_core.models.baze_class import BaseClass


# @dataclass
# class t:
#     dt: str
#     tr: Traffic
#

@dataclass
class TrafficExtended(BaseClass):
    id: int
    # ticks: Dict
    ticks: Dict[str, Traffic]
    total: Traffic
