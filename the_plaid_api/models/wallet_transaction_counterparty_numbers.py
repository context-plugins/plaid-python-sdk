from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .wallet_transaction_counterparty_bacs import (
    WalletTransactionCounterpartyBacs,
    WalletTransactionCounterpartyBacsDict,
)
from .wallet_transaction_counterparty_international import (
    WalletTransactionCounterpartyInternational,
    WalletTransactionCounterpartyInternationalDict,
)


class WalletTransactionCounterpartyNumbers(SdkBaseModel):
    """The counterparty's bank account numbers. Exactly one of IBAN or Bacs data is required."""

    bacs: OptionalNullable[WalletTransactionCounterpartyBacs] = UNSET
    """The account number and sort code of the counterparty's account"""

    international: OptionalNullable[WalletTransactionCounterpartyInternational] = UNSET
    """International Bank Account Number for a Wallet Transaction"""


class WalletTransactionCounterpartyNumbersDict(TypedDict):
    bacs: NotRequired[WalletTransactionCounterpartyBacsDict | None]
    international: NotRequired[WalletTransactionCounterpartyInternationalDict | None]
