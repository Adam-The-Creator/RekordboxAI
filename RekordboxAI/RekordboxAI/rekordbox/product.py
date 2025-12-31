from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    def __init__(
        self,
        name:           Optional[str],
        version:        Optional[str],
        company:        Optional[str]
    ):
        self.name       = name
        self.version    = version
        self.company    = company
