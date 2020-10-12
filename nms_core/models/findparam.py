from dataclasses import dataclass
from typing import Dict


@dataclass
class FindParams:
    object: str
    where: Dict

