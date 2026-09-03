from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PoboxStatus(str, Enum):
    """Field describing whether the associated address is a post office box. Will be ``yes`` when a P.O. box is
    detected, ``no`` when Plaid confirmed the address is not a P.O. box, and ``no_data`` when Plaid was not able to
    determine if the address is a P.O. box."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


PoboxStatusOrStr: TypeAlias = Annotated[PoboxStatus | str, open_enum_validator(PoboxStatus)]
