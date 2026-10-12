from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .link_delivery_options import LinkDeliveryOptions, LinkDeliveryOptionsDict


class LinkDeliveryCreateRequest(SdkBaseModel):
    """LinkDeliveryCreateRequest defines the request schema for ``/link_delivery/create``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    link_token: str
    """A ``link_token`` from a previous invocation of ``/link/token/create``."""

    options: Optional[LinkDeliveryOptions] = UNSET
    """Optional metadata related to the Hosted Link session"""


class LinkDeliveryCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    link_token: str
    options: NotRequired[LinkDeliveryOptionsDict]
