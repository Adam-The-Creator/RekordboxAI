from dataclasses import dataclass
from enum import IntEnum
from typing import Optional, List


class NodeType(IntEnum):
    FOLDER      = 0
    PLAYLIST    = 1


@dataclass
class Node:
    def __init__(
        self,
        type:           Optional[NodeType],
        name:           Optional[str]
    ):
        self.type       = type
        self.name       = name


@dataclass
class FolderNode(Node):
    def __init__(
        self,
        name:           Optional[str],
        count:          Optional[int],
        nodes:          Optional[List[Node]]
        ):
        super().__init__(NodeType.FOLDER, name)
        self.count      = count
        self.nodes      = nodes


@dataclass
class PlaylistNode(Node):
    def __init__(
        self,
        name:           Optional[str],
        entries:        Optional[int],
        key_type:       Optional[int],
        track_keys:     Optional[List[str]]
        ):
        super().__init__(NodeType.PLAYLIST, name)
        self.entries    = entries
        self.key_type   = key_type
        self.track_keys = track_keys