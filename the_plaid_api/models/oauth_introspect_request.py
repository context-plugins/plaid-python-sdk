from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OauthIntrospectRequest(SdkBaseModel):
    """OAuth token introspect request."""

    token: str
    """An OAuth token of any type (``refresh_token``, ``access_token``, etc)"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    client_secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body as either ``secret`` or ``client_secret``."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body as either ``secret`` or ``client_secret``."""


class OauthIntrospectRequestDict(TypedDict):
    token: str
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
    secret: NotRequired[str]
