from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PartyType(str, Enum):
    """Identifies the type of a party"""

    DATA_ACCESS_PLATFORM = "DATA_ACCESS_PLATFORM"
    DATA_PROVIDER = "DATA_PROVIDER"
    DATA_RECIPIENT = "DATA_RECIPIENT"
    INDIVIDUAL = "INDIVIDUAL"
    MERCHANT = "MERCHANT"
    VENDOR = "VENDOR"

    __str__ = str.__str__


PartyTypeOrStr: TypeAlias = Annotated[PartyType | str, open_enum_validator(PartyType)]
