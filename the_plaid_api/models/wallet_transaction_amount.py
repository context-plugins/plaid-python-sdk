from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.iso_currency_code import IsoCurrencyCodeOrStr


class WalletTransactionAmount(SdkBaseModel):
    """The amount and currency of a transaction"""

    iso_currency_code: IsoCurrencyCodeOrStr
    """An ISO-4217 currency code, used with e-wallets and transactions."""

    value: float
    """The amount of the transaction. Must contain at most two digits of precision e.g. ``1.23``."""


class WalletTransactionAmountDict(TypedDict):
    iso_currency_code: IsoCurrencyCodeOrStr
    value: float
