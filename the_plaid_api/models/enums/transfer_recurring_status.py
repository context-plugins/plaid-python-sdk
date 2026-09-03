from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferRecurringStatus(str, Enum):
    """The status of the recurring transfer.

    ``active``: The recurring transfer is currently active. ``cancelled``: The recurring transfer was cancelled by the
    client or Plaid. ``expired``: The recurring transfer has completed all originations according to its recurring
    schedule."""

    ACTIVE = "active"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

    __str__ = str.__str__


TransferRecurringStatusOrStr: TypeAlias = Annotated[
    TransferRecurringStatus | str, open_enum_validator(TransferRecurringStatus)
]
