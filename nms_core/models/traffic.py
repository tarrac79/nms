from dataclasses import dataclass
from nms_core.models.baze_class import BaseClass


@dataclass
class Traffic(BaseClass):
    tx_low: int
    tx_2: int
    tx_3: int
    tx_med: int
    tx_5: int
    tx_6: int
    tx_high: int

    rx_low: int
    rx_2: int
    rx_3: int
    rx_med: int
    rx_5: int
    rx_6: int
    rx_high: int

    @property
    def tx(self):
        return self.tx_low + self.tx_2 + self.tx_3 + self.tx_med + self.tx_5 + self.tx_6 + self.tx_high

    @property
    def rx(self):
        return self.rx_low + self.rx_2 + self.rx_3 + self.rx_med + self.rx_5 + self.rx_6 + self.rx_high


