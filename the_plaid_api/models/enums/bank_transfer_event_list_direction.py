from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferEventListDirection(str, Enum):
    """Indicates the direction of the transfer: ``outbound``: for API-initiated transfers ``inbound``: for payments
    received by the FBO account."""

    INBOUND = "inbound"
    OUTBOUND = "outbound"

    __str__ = str.__str__


BankTransferEventListDirectionOrStr: TypeAlias = Annotated[
    BankTransferEventListDirection | str, open_enum_validator(BankTransferEventListDirection)
]
