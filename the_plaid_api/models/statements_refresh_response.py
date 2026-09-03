from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StatementsRefreshResponse(SdkBaseModel):
    """StatementsRefreshResponse defines the response schema for ``/statements/refresh``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class StatementsRefreshResponseDict(TypedDict):
    request_id: str
