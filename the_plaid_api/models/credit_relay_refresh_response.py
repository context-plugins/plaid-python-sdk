from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditRelayRefreshResponse(SdkBaseModel):
    """CreditRelayRefreshResponse defines the response schema for ``/credit/relay/refresh``"""

    relay_token: str
    asset_report_id: Optional[str] = UNSET
    """A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditRelayRefreshResponseDict(TypedDict):
    relay_token: str
    asset_report_id: NotRequired[str]
    request_id: str
