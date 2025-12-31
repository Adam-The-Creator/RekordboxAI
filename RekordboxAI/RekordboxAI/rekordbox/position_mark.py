from dataclasses import dataclass
from typing import Optional
from enum import IntEnum


class PositionMarkType(IntEnum):
    CUE         = 0
    FADE_IN     = 1
    FADE_OUT    = 2
    LOAD        = 3
    LOOP        = 4


@dataclass
class PositionMark:
    def __init__(
        self,
        name:       Optional[str],
        type:       Optional[PositionMarkType],
        start:      Optional[float],
        end:        Optional[float],
        num:        Optional[int]
    ):
        self.name   = name
        self.type   = type
        self.start  = start
        self.end    = end
        self.num    = num