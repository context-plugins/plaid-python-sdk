from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditRelayRemoveRequest(SdkBaseModel):
    """CreditRelayRemoveRequest defines the request schema for ``/credit/relay/remove``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    relay_token: str
    """The ``relay_token`` you would like to revoke."""


class CreditRelayRemoveRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    relay_token: str
