from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProtectUserInsightsGetRequest(SdkBaseModel):
    """Request object for /protect/user/insights/get"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user_id: Optional[str] = UNSET
    """The Plaid User ID. Either ``user_id`` or ``client_user_id`` must be provided."""

    client_user_id: Optional[str] = UNSET
    """A unique ID representing the end user. Either ``user_id`` or ``client_user_id`` must be provided."""


class ProtectUserInsightsGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_id: NotRequired[str]
    client_user_id: NotRequired[str]
