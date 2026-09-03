from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UserThirdPartyTokenCreateResponse(SdkBaseModel):
    """UserThirdPartyTokenCreateResponse defines the response schema for ``/user/third_party_token/create``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    third_party_user_token: str
    """The third-party user token associated with the requested User data."""


class UserThirdPartyTokenCreateResponseDict(TypedDict):
    request_id: str
    third_party_user_token: str
