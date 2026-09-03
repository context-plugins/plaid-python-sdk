from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .liabilities_get_request_options import LiabilitiesGetRequestOptions, LiabilitiesGetRequestOptionsDict


class LiabilitiesGetRequest(SdkBaseModel):
    """LiabilitiesGetRequest defines the request schema for ``/liabilities/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    options: Optional[LiabilitiesGetRequestOptions] = UNSET
    """An optional object to filter ``/liabilities/get`` results. If provided, ``options`` cannot be null."""


class LiabilitiesGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    options: NotRequired[LiabilitiesGetRequestOptions | LiabilitiesGetRequestOptionsDict]
