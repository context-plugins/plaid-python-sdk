from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EnrichTransactionDirection(str, Enum):
    """The direction of the transaction from the perspective of the account holder:

    ``OUTFLOW`` - Includes outgoing transfers, purchases, and fees. (Typically represented as a negative value on
    checking accounts and debit cards and a positive value on credit cards.)

    ``INFLOW`` - Includes incoming transfers, refunds, and income. (Typically represented as a positive value on
    checking accounts and debit cards and a negative value on credit cards.)"""

    INFLOW = "INFLOW"
    OUTFLOW = "OUTFLOW"

    __str__ = str.__str__


EnrichTransactionDirectionOrStr: TypeAlias = Annotated[
    EnrichTransactionDirection | str, open_enum_validator(EnrichTransactionDirection)
]
