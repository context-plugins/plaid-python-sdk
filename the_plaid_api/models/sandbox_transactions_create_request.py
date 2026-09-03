from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_sandbox_transaction import CustomSandboxTransaction, CustomSandboxTransactionDict


class SandboxTransactionsCreateRequest(SdkBaseModel):
    """SandboxTransactionsCreateRequest defines the request schema for ``/sandbox/transactions/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    transactions: list[CustomSandboxTransaction]
    """List of transactions to be added"""


class SandboxTransactionsCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    transactions: list[CustomSandboxTransaction | CustomSandboxTransactionDict]
