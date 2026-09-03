from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StandaloneInvestmentTransactionTransferType(str, Enum):
    """Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer"""

    ASSIGNMENT = "assignment"
    ADJUSTMENT = "adjustment"
    EXERCISE = "exercise"
    EXPIRE = "expire"
    MERGER = "merger"
    REQUEST = "request"
    SEND = "send"
    SPIN_OFF = "spin off"
    SPLIT = "split"
    TRADE = "trade"
    TRANSFER = "transfer"

    __str__ = str.__str__


StandaloneInvestmentTransactionTransferTypeOrStr: TypeAlias = Annotated[
    StandaloneInvestmentTransactionTransferType | str, open_enum_validator(StandaloneInvestmentTransactionTransferType)
]
