from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SignalPrepareResponse(SdkBaseModel):
    """SignalPrepareResponse defines the response schema for ``/signal/prepare``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SignalPrepareResponseDict(TypedDict):
    request_id: str
