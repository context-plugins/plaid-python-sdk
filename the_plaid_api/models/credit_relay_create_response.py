from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreditRelayCreateResponse(SdkBaseModel):
    """CreditRelayCreateResponse defines the response schema for ``/credit/relay/create``"""

    relay_token: str
    """A token that can be shared with a third party to allow them to access the Asset Report. This token should be
    stored securely."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditRelayCreateResponseDict(TypedDict):
    relay_token: str
    request_id: str
