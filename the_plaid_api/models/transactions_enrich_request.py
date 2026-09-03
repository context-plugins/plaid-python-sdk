from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .client_provided_transaction import ClientProvidedTransaction, ClientProvidedTransactionDict
from .transactions_enrich_request_options import TransactionsEnrichRequestOptions, TransactionsEnrichRequestOptionsDict


class TransactionsEnrichRequest(SdkBaseModel):
    """TransactionsEnrichRequest defines the request schema for ``/transactions/enrich``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    account_type: str
    """The account type for the requested transactions (either ``depository`` or ``credit``)."""

    transactions: list[ClientProvidedTransaction]
    """An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request."""

    options: Optional[TransactionsEnrichRequestOptions] = UNSET
    """An optional object to be used with the request."""


class TransactionsEnrichRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    account_type: str
    transactions: list[ClientProvidedTransaction | ClientProvidedTransactionDict]
    options: NotRequired[TransactionsEnrichRequestOptions | TransactionsEnrichRequestOptionsDict]
