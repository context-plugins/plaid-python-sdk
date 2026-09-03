from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserAccountSessionEventSendResponse(SdkBaseModel):
    """UserAccountSessionEventSendResponse defines the response schema for ``/user_account/session/event/send``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class UserAccountSessionEventSendResponseDict(TypedDict):
    request_id: str
