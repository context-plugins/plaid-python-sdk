from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ForwardedJsonresponse(SdkBaseModel):
    """An arbitrary JSON payload sent to or received from the Plaid server. Internal use only."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ForwardedJsonresponseDict(TypedDict):
    request_id: str
