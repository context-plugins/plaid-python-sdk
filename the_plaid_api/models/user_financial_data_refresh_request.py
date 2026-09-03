from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UserFinancialDataRefreshRequest(SdkBaseModel):
    """UserFinancialDataRefreshRequest defines the request schema for ``/user/financial_data/refresh``"""

    user_id: str
    """A Plaid-generated ID that identifies the end user."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class UserFinancialDataRefreshRequestDict(TypedDict):
    user_id: str
    client_id: NotRequired[str]
    secret: NotRequired[str]
