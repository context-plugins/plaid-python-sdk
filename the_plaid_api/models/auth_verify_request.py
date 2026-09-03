from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .auth_verify_request_numbers import AuthVerifyRequestNumbers, AuthVerifyRequestNumbersDict


class AuthVerifyRequest(SdkBaseModel):
    """AuthVerifyRequest defines the request schema for ``/auth/verify``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    legal_name: OptionalNullable[str] = UNSET
    """Account owner's legal name"""

    numbers: AuthVerifyRequestNumbers
    """An object containing identifying account numbers for verification via Database Auth"""


class AuthVerifyRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    legal_name: NotRequired[str | None]
    numbers: AuthVerifyRequestNumbers | AuthVerifyRequestNumbersDict
