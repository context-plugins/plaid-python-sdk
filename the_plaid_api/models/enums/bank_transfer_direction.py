from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferDirection(str, Enum):
    """Indicates the direction of the transfer: ``outbound`` for API-initiated transfers, or ``inbound`` for payments
    received by the FBO account."""

    OUTBOUND = "outbound"
    INBOUND = "inbound"

    __str__ = str.__str__


BankTransferDirectionOrStr: TypeAlias = Annotated[
    BankTransferDirection | str, open_enum_validator(BankTransferDirection)
]
