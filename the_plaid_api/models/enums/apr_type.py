from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AprType(str, Enum):
    """The type of balance to which the APR applies."""

    BALANCE_TRANSFER_APR = "balance_transfer_apr"
    CASH_APR = "cash_apr"
    PURCHASE_APR = "purchase_apr"
    SPECIAL = "special"

    __str__ = str.__str__


AprTypeOrStr: TypeAlias = Annotated[AprType | str, open_enum_validator(AprType)]
