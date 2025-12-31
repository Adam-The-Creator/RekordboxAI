from dataclasses import dataclass
from typing import Optional

from rekordbox.collection import Collection
from rekordbox.playlists import Playlists
from rekordbox.product import Product


@dataclass
class DJPlaylists:
    def __init__(
        self,
        version:    Optional[str],
        product:    Optional[Product],
        collection: Optional[Collection],
        playlists:  Optional[Playlists],
    ):
        self.version    = version
        self.product    = product
        self.collection = collection
        self.playlists  = playlists