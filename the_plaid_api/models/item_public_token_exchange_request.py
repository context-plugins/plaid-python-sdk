from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemPublicTokenExchangeRequest(SdkBaseModel):
    """ItemPublicTokenExchangeRequest defines the request schema for ``/item/public_token/exchange``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    public_token: str
    """Your ``public_token``, obtained from the Link ``onSuccess`` callback or ``/sandbox/public_token/create``."""


class ItemPublicTokenExchangeRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    public_token: str
