from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DepositoryAccountSubtype(str, Enum):
    """Valid account subtypes for depository accounts. For a list containing descriptions of each subtype, see `Account
    schemas <https://plaid.com/docs/api/accounts/#StandaloneAccountType-depository>`__."""

    CHECKING = "checking"
    SAVINGS = "savings"
    HSA = "hsa"
    CD = "cd"
    MONEY_MARKET = "money market"
    PAYPAL = "paypal"
    PREPAID = "prepaid"
    CASH_MANAGEMENT = "cash management"
    EBT = "ebt"
    LIMITED_PURPOSE_CHECKING = "limited purpose checking"
    ALL = "all"

    __str__ = str.__str__


DepositoryAccountSubtypeOrStr: TypeAlias = Annotated[
    DepositoryAccountSubtype | str, open_enum_validator(DepositoryAccountSubtype)
]
