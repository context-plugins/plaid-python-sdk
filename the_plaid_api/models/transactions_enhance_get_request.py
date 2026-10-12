from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .client_provided_raw_transaction import ClientProvidedRawTransaction, ClientProvidedRawTransactionDict


class TransactionsEnhanceGetRequest(SdkBaseModel):
    """TransactionsEnhanceGetRequest defines the request schema for ``/beta/transactions/v1/enhance``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    account_type: str
    """The type of account for the requested transactions (``depository`` or ``credit``)."""

    transactions: list[ClientProvidedRawTransaction]
    """An array of raw transactions to be enhanced."""


class TransactionsEnhanceGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    account_type: str
    transactions: list[ClientProvidedRawTransactionDict]
