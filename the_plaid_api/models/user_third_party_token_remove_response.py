from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserThirdPartyTokenRemoveResponse(SdkBaseModel):
    """UserThirdPartyTokenRemoveResponse defines the response schema for ``/user/third_party_token/remove``"""

    removed: bool
    """``true`` if the third-party user token was successfully removed."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class UserThirdPartyTokenRemoveResponseDict(TypedDict):
    removed: bool
    request_id: str
