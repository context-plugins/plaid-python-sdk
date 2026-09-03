from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferNetwork(str, Enum):
    """The network or rails used for the transfer. Valid options are ``ach``, ``same-day-ach``, or ``wire``."""

    ACH = "ach"
    SAME_DAY_ACH = "same-day-ach"
    WIRE = "wire"

    __str__ = str.__str__


BankTransferNetworkOrStr: TypeAlias = Annotated[BankTransferNetwork | str, open_enum_validator(BankTransferNetwork)]
