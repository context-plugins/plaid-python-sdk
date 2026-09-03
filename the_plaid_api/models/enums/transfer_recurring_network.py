from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferRecurringNetwork(str, Enum):
    """Networks eligible for recurring transfers."""

    ACH = "ach"
    SAME_DAY_ACH = "same-day-ach"
    RTP = "rtp"

    __str__ = str.__str__


TransferRecurringNetworkOrStr: TypeAlias = Annotated[
    TransferRecurringNetwork | str, open_enum_validator(TransferRecurringNetwork)
]
