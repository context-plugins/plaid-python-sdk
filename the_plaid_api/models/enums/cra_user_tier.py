from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraUserTier(str, Enum):
    """The tier of the user."""

    FREE = "free"
    PAID = "paid"

    __str__ = str.__str__


CraUserTierOrStr: TypeAlias = Annotated[CraUserTier | str, open_enum_validator(CraUserTier)]
