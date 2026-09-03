from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SweepStatus(str, Enum):
    """The status of a sweep transfer

    ``"pending"`` - The sweep is currently pending ``"posted"`` - The sweep has been posted ``"settled"`` - The sweep
    has settled. This is the terminal state of a successful credit sweep. ``"returned"`` - The sweep has been returned.
    This is the terminal state of a returned sweep. Returns of a sweep are extremely rare, since sweeps are money
    movement between your own bank account and your own Ledger. ``"funds_available"`` - Funds from the sweep have been
    released from hold and applied to the ledger's available balance. (Only applicable to deposits.) This is the
    terminal state of a successful deposit sweep. ``"failed"`` - The sweep has failed. This is the terminal state of a
    failed sweep."""

    PENDING = "pending"
    POSTED = "posted"
    SETTLED = "settled"
    FUNDS_AVAILABLE = "funds_available"
    RETURNED = "returned"
    FAILED = "failed"

    __str__ = str.__str__


SweepStatusOrStr: TypeAlias = Annotated[SweepStatus | str, open_enum_validator(SweepStatus)]
