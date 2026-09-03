from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetInvestmentTransactionType(str, Enum):
    """Asset Investment Transaction Type Enumerated derived by Vendor."""

    BUY = "Buy"
    SELL = "Sell"
    DIVIDENDS = "Dividends"
    INTEREST = "Interest"
    TRANSFERS = "Transfers"
    REINVESTMENTS = "Reinvestments"
    FUNDS_RECEIVED = "FundsReceived"
    OTHER = "Other"

    __str__ = str.__str__


AssetInvestmentTransactionTypeOrStr: TypeAlias = Annotated[
    AssetInvestmentTransactionType | str, open_enum_validator(AssetInvestmentTransactionType)
]
