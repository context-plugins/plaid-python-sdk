from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferStatus(str, Enum):
    """The status of the transfer."""

    PENDING = "pending"
    POSTED = "posted"
    CANCELLED = "cancelled"
    FAILED = "failed"
    REVERSED = "reversed"

    __str__ = str.__str__


BankTransferStatusOrStr: TypeAlias = Annotated[BankTransferStatus | str, open_enum_validator(BankTransferStatus)]
