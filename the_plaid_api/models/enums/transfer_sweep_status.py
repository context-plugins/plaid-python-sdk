from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferSweepStatus(str, Enum):
    """The status of the sweep for the transfer.

    ``unswept``: The transfer hasn't been swept yet. ``swept``: The transfer was swept to the sweep account.
    ``swept_settled``: Credits are available to be withdrawn or debits have been deducted from the customer's business
    checking account. ``return_swept``: The transfer was returned, funds were pulled back or pushed back to the sweep
    account. ``null``: The transfer will never be swept (e.g. if the transfer is cancelled or returned before being
    swept)"""

    UNSWEPT = "unswept"
    SWEPT = "swept"
    SWEPT_SETTLED = "swept_settled"
    RETURN_SWEPT = "return_swept"

    __str__ = str.__str__


TransferSweepStatusOrStr: TypeAlias = Annotated[TransferSweepStatus | str, open_enum_validator(TransferSweepStatus)]
