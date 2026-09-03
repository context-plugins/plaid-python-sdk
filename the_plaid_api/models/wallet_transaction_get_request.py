from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WalletTransactionGetRequest(SdkBaseModel):
    """WalletTransactionGetRequest defines the request schema for ``/wallet/transaction/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    transaction_id: str
    """The ID of the transaction to fetch"""


class WalletTransactionGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    transaction_id: str
