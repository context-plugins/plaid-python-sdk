from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UserThirdPartyTokenRemoveRequest(SdkBaseModel):
    """UserThirdPartyTokenRemoveRequest defines the request schema for ``/user/third_party_token/remove``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    third_party_user_token: str
    """The third-party user token associated with the requested User data."""


class UserThirdPartyTokenRemoveRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    third_party_user_token: str
