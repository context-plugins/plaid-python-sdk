from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .payment_initiation_address import PaymentInitiationAddress, PaymentInitiationAddressDict
from .wallet_transaction_counterparty_numbers import (
    WalletTransactionCounterpartyNumbers,
    WalletTransactionCounterpartyNumbersDict,
)


class WalletTransactionCounterparty(SdkBaseModel):
    """An object representing the e-wallet transaction's counterparty"""

    name: str
    """The name of the counterparty"""

    numbers: WalletTransactionCounterpartyNumbers
    """The counterparty's bank account numbers. Exactly one of IBAN or Bacs data is required."""

    address: OptionalNullable[PaymentInitiationAddress] = UNSET
    """The optional address of the payment recipient's bank account. Required by most institutions outside of the UK."""

    date_of_birth: OptionalNullable[Date] = UNSET
    """The counterparty's birthdate, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD) format."""


class WalletTransactionCounterpartyDict(TypedDict):
    name: str
    numbers: WalletTransactionCounterpartyNumbers | WalletTransactionCounterpartyNumbersDict
    address: NotRequired[PaymentInitiationAddress | PaymentInitiationAddressDict | None]
    date_of_birth: NotRequired[Date | None]
