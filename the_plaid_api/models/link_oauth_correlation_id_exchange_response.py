from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkOauthCorrelationIdExchangeResponse(SdkBaseModel):
    """LinkOAuthCorrelationIdExchangeResponse defines the response schema for ``/link/oauth/correlation_id/exchange``"""

    link_token: str
    """The ``link_token`` associated to the given ``link_correlation_id``, which can be used to re-initialize Link."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class LinkOauthCorrelationIdExchangeResponseDict(TypedDict):
    link_token: str
    request_id: str
