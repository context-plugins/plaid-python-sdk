from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SandboxPaymentProfileResetLoginRequest(SdkBaseModel):
    """SandboxPaymentProfileResetLoginRequest defines the request schema for ``/sandbox/payment_profile/reset_login``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    payment_profile_token: str
    """A payment profile token associated with the Payment Profile data that is being requested."""


class SandboxPaymentProfileResetLoginRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    payment_profile_token: str
