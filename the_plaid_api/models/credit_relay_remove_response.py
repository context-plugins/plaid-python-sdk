from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditRelayRemoveResponse(SdkBaseModel):
    """CreditRelayRemoveResponse defines the response schema for ``/credit/relay/remove``"""

    removed: bool
    """``true`` if the relay token was successfully removed."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditRelayRemoveResponseDict(TypedDict):
    removed: bool
    request_id: str
