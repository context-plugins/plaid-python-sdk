from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.buy_type import BuyTypeOrStr
from .enums.cash_type import CashTypeOrStr
from .enums.fee_type import FeeTypeOrStr
from .enums.sell_type import SellTypeOrStr
from .enums.standalone_investment_transaction_transfer_type import StandaloneInvestmentTransactionTransferTypeOrStr


class StandaloneInvestmentTransactionType(SdkBaseModel):
    """Valid values for investment transaction types and subtypes. Note that transactions representing inflow of cash
    will appear as negative amounts, outflow of cash will appear as positive amounts."""

    buy: BuyTypeOrStr
    """Buying an investment"""

    sell: SellTypeOrStr
    """Selling an investment"""

    cancel: str
    """A cancellation of a pending transaction"""

    cash: CashTypeOrStr
    """Activity that modifies a cash position"""

    fee: FeeTypeOrStr
    """Fees on the account, e.g. commission, bookkeeping, options-related."""

    transfer: StandaloneInvestmentTransactionTransferTypeOrStr
    """Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer"""


class StandaloneInvestmentTransactionTypeDict(TypedDict):
    buy: BuyTypeOrStr
    sell: SellTypeOrStr
    cancel: str
    cash: CashTypeOrStr
    fee: FeeTypeOrStr
    transfer: StandaloneInvestmentTransactionTransferTypeOrStr
