from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartyRegistry(str, Enum):
    """The registry containing the party's registration with name and id"""

    FDX = "FDX"
    GLEIF = "GLEIF"
    ICANN = "ICANN"
    PRIVATE = "PRIVATE"

    __str__ = str.__str__


PartyRegistryOrStr: TypeAlias = Annotated[PartyRegistry | str, open_enum_validator(PartyRegistry)]
