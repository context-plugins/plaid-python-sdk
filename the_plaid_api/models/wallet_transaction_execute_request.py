from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .originating_fund_source import OriginatingFundSource, OriginatingFundSourceDict
from .wallet_transaction_amount import WalletTransactionAmount, WalletTransactionAmountDict
from .wallet_transaction_counterparty import WalletTransactionCounterparty, WalletTransactionCounterpartyDict


class WalletTransactionExecuteRequest(SdkBaseModel):
    """WalletTransactionExecuteRequest defines the request schema for ``/wallet/transaction/execute``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    idempotency_key: str
    """A random key provided by the client, per unique wallet transaction. Maximum of 128 characters.

    The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
    If a request to execute a wallet transaction fails due to a network connection error, then after a minimum delay of
    one minute, you can retry the request with the same idempotency key to guarantee that only a single wallet
    transaction is created. If the request was successfully processed, it will prevent any transaction that uses the
    same idempotency key, and was received within 24 hours of the first request, from being processed."""

    wallet_id: str
    """The ID of the e-wallet to debit from"""

    counterparty: WalletTransactionCounterparty
    """An object representing the e-wallet transaction's counterparty"""

    amount: WalletTransactionAmount
    """The amount and currency of a transaction"""

    reference: str
    """A reference for the transaction. This must be an alphanumeric string with 6 to 18 characters and must not contain
    any special characters or spaces. Ensure that the ``reference`` field is unique for each transaction."""

    originating_fund_source: OptionalNullable[OriginatingFundSource] = UNSET
    """The original source of the funds. This field is required by local regulation for certain businesses (e.g. money
    remittance) to send payouts to recipients in the EU and UK."""


class WalletTransactionExecuteRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    idempotency_key: str
    wallet_id: str
    counterparty: WalletTransactionCounterpartyDict
    amount: WalletTransactionAmountDict
    reference: str
    originating_fund_source: NotRequired[OriginatingFundSourceDict | None]
