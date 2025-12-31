from dataclasses import dataclass
from typing import Optional, List

from rekordbox.track import Track


@dataclass
class Collection:
    def __init__(
        self,
        entries:    Optional[int],
        tracks:     Optional[List[Track]],
    ):
        self.entries    = entries
        self.tracks     = tracks