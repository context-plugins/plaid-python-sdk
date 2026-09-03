from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WalletBalance(SdkBaseModel):
    """An object representing the e-wallet balance"""

    iso_currency_code: str
    """The ISO-4217 currency code of the balance"""

    current: float
    """The total amount of funds in the account"""

    available: float
    """The total amount of funds in the account after subtracting pending debit transaction amounts"""


class WalletBalanceDict(TypedDict):
    iso_currency_code: str
    current: float
    available: float
