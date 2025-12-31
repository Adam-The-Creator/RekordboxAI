from dataclasses import dataclass
from typing import Optional, List

from rekordbox.node import Node


@dataclass
class Playlists:
    def __init__(
        self,
        nodes:          Optional[List[Node]]
    ):
        self.nodes      = nodes
