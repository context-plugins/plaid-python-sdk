from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransactionsRulesListRequest(SdkBaseModel):
    """TransactionsRulesListRequest defines the request schema for ``/beta/transactions/rules/v1/list``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    client_user_id: str
    """A unique ID representing the end user whose rules should be listed."""


class TransactionsRulesListRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    client_user_id: str
