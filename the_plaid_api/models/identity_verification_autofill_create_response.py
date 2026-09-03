from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.identity_verification_autofill_status import IdentityVerificationAutofillStatusOrStr
from .identity_verification_autofill_user_data import (
    IdentityVerificationAutofillUserData,
    IdentityVerificationAutofillUserDataDict,
)


class IdentityVerificationAutofillCreateResponse(SdkBaseModel):
    """Autofill represents unverified customer information. This needs to be confirmed by the customer before using."""

    status: IdentityVerificationAutofillStatusOrStr
    """A status enum indicating whether autofill succeeded or failed."""

    user: IdentityVerificationAutofillUserData | None
    """User information that was autofilled. All this information should be confirmed by the user before using."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class IdentityVerificationAutofillCreateResponseDict(TypedDict):
    status: IdentityVerificationAutofillStatusOrStr
    user: IdentityVerificationAutofillUserData | IdentityVerificationAutofillUserDataDict | None
    request_id: str
