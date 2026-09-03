from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class HoldingTaxLotPositionType(str, Enum):
    """Indicates whether a holding lot position is long or short. Possible values are ``LONG`` and ``SHORT``."""

    LONG = "LONG"
    SHORT = "SHORT"

    __str__ = str.__str__


HoldingTaxLotPositionTypeOrStr: TypeAlias = Annotated[
    HoldingTaxLotPositionType | str, open_enum_validator(HoldingTaxLotPositionType)
]
