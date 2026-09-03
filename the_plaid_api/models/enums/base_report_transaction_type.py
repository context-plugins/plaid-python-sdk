from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BaseReportTransactionType(str, Enum):
    """``digital:`` transactions that took place online.

    ``place:`` transactions that were made at a physical location.

    ``special:`` transactions that relate to banks, e.g. fees or deposits.

    ``unresolved:`` transactions that do not fit into the other types."""

    DIGITAL = "digital"
    PLACE = "place"
    SPECIAL = "special"
    UNRESOLVED = "unresolved"

    __str__ = str.__str__


BaseReportTransactionTypeOrStr: TypeAlias = Annotated[
    BaseReportTransactionType | str, open_enum_validator(BaseReportTransactionType)
]
