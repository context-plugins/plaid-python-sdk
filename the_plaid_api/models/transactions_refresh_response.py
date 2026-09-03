from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TransactionsRefreshResponse(SdkBaseModel):
    """TransactionsRefreshResponse defines the response schema for ``/transactions/refresh``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class TransactionsRefreshResponseDict(TypedDict):
    request_id: str
