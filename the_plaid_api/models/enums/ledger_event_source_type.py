from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LedgerEventSourceType(str, Enum):
    """Source of the ledger event.

    ``"TRANSFER"`` - The source of the ledger event is a transfer ``"SWEEP"`` - The source of the ledger event is a
    sweep ``"REFUND"`` - The source of the ledger event is a refund"""

    TRANSFER = "TRANSFER"
    SWEEP = "SWEEP"
    REFUND = "REFUND"

    __str__ = str.__str__


LedgerEventSourceTypeOrStr: TypeAlias = Annotated[
    LedgerEventSourceType | str, open_enum_validator(LedgerEventSourceType)
]
