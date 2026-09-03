from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .investments_auth_get_request_options import InvestmentsAuthGetRequestOptions, InvestmentsAuthGetRequestOptionsDict


class InvestmentsAuthGetRequest(SdkBaseModel):
    """InvestmentsAuthGetRequest defines the request schema for ``/investments/auth/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    options: Optional[InvestmentsAuthGetRequestOptions] = UNSET
    """An optional object to filter ``/investments/auth/get`` results."""


class InvestmentsAuthGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    options: NotRequired[InvestmentsAuthGetRequestOptions | InvestmentsAuthGetRequestOptionsDict]
