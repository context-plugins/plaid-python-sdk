from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .auth_get_request_options import AuthGetRequestOptions, AuthGetRequestOptionsDict


class AuthGetRequest(SdkBaseModel):
    """AuthGetRequest defines the request schema for ``/auth/get``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    options: Optional[AuthGetRequestOptions] = UNSET
    """An optional object to filter ``/auth/get`` results."""


class AuthGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    options: NotRequired[AuthGetRequestOptions | AuthGetRequestOptionsDict]
