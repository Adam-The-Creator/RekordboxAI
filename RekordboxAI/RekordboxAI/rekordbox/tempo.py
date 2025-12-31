from dataclasses import dataclass
from typing import Optional


@dataclass
class Tempo:
    def __init__(
        self,
        inizio:     Optional[float],
        bpm:        Optional[float],
        metro:      Optional[str],
        battito:    Optional[int]
    ):
        self.inizio     = inizio
        self.bpm        = bpm
        self.metro      = metro
        self.battito    = battito