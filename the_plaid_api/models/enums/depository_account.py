from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DepositoryAccount(str, Enum):
    """An account type holding cash, in which funds are deposited."""

    CASH_MANAGEMENT = "cash management"
    CD = "cd"
    CHECKING = "checking"
    EBT = "ebt"
    HSA = "hsa"
    LIMITED_PURPOSE_CHECKING = "limited purpose checking"
    MONEY_MARKET = "money market"
    PAYPAL = "paypal"
    PREPAID = "prepaid"
    SAVINGS = "savings"

    __str__ = str.__str__


DepositoryAccountOrStr: TypeAlias = Annotated[DepositoryAccount | str, open_enum_validator(DepositoryAccount)]
