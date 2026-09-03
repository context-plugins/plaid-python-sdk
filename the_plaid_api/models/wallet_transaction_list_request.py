from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .wallet_transaction_list_request_options import (
    WalletTransactionListRequestOptions,
    WalletTransactionListRequestOptionsDict,
)


class WalletTransactionListRequest(SdkBaseModel):
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
    """A value representing the latest transaction to be included in the response. Set this from ``next_cursor``
    received in the previous ``/wallet/transaction/list`` request. If provided, the response will only contain that
    transaction and transactions created before it. If omitted, the response will contain transactions starting from the
    most recent, and in descending order by the ``created_at`` time."""

    count: Optional[int] = UNSET
    """The number of transactions to fetch"""

    options: OptionalNullable[WalletTransactionListRequestOptions] = UNSET
    """Additional wallet transaction options"""


class WalletTransactionListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    wallet_id: str
    cursor: NotRequired[str]
    count: NotRequired[int]
    options: NotRequired[WalletTransactionListRequestOptions | WalletTransactionListRequestOptionsDict | None]
