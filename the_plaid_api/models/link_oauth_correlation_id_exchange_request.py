from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LinkOauthCorrelationIdExchangeRequest(SdkBaseModel):
    """LinkOAuthCorrelationIdExchangeRequest defines the request schema for ``/link/oauth/correlation_id/exchange``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    link_correlation_id: str
    """A ``link_correlation_id`` from a received OAuth redirect URI callback"""


class LinkOauthCorrelationIdExchangeRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    link_correlation_id: str
