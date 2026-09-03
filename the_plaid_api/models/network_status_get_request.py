from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .network_status_get_user import NetworkStatusGetUser, NetworkStatusGetUserDict


class NetworkStatusGetRequest(SdkBaseModel):
    """NetworkStatusGetRequest defines the request schema for ``/network/status/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user: NetworkStatusGetUser
    """An object specifying information about the end user for the network status check."""

    template_id: Optional[str] = UNSET
    """The id of a template defined in Plaid Dashboard. This field is used if you have additional criteria that you want
    to check against (e.g. Layer eligibility)."""


class NetworkStatusGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user: NetworkStatusGetUser | NetworkStatusGetUserDict
    template_id: NotRequired[str]
