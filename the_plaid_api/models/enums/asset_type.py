from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetType(str, Enum):
    """A value from a MISMO prescribed list that specifies financial assets in a mortgage loan transaction. Assets may
    be either liquid or fixed and are associated with a corresponding asset amount."""

    CHECKING_ACCOUNT = "CheckingAccount"
    SAVINGS_ACCOUNT = "SavingsAccount"
    INVESTMENT = "Investment"
    MONEY_MARKET_FUND = "MoneyMarketFund"
    OTHER = "Other"

    __str__ = str.__str__


AssetTypeOrStr: TypeAlias = Annotated[AssetType | str, open_enum_validator(AssetType)]
