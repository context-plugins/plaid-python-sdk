from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .wallet_transaction_list_request_options import (
    WalletTransactionListRequestOptions,
    WalletTransactionListRequestOptionsDict,
)


class WalletTransactionsListRequest(SdkBaseModel):
    """WalletTransactionListRequest defines the request schema for ``/wallet/transaction/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    wallet_id: str
    """The ID of the e-wallet to fetch transactions from"""

    cursor: Optional[str] = UNSET
    """A base64 value representing the latest transaction that has already been requested. Set this to ``next_cursor``
    received from the previous ``/wallet/transaction/list`` request. If provided, the response will only contain
    transactions created before that transaction. If omitted, the response will contain transactions starting from the
    most recent, and in descending order by the ``created_at`` time."""

    count: int = 10
    """The number of transactions to fetch"""

    options: OptionalNullable[WalletTransactionListRequestOptions] = UNSET
    """Additional wallet transaction options"""


class WalletTransactionsListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    wallet_id: str
    cursor: NotRequired[str]
    count: NotRequired[int]
    options: NotRequired[WalletTransactionListRequestOptionsDict | None]
