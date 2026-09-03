from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IdentityVerificationAutofillCreateRequest(SdkBaseModel):
    """Request input to autofill an Identity Verification"""

    identity_verification_id: str
    """ID of the associated Identity Verification attempt."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""


class IdentityVerificationAutofillCreateRequestDict(TypedDict):
    identity_verification_id: str
    client_id: NotRequired[str]
    secret: NotRequired[str]
