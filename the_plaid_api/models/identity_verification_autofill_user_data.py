from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .identity_verification_autofill_address import (
    IdentityVerificationAutofillAddress,
    IdentityVerificationAutofillAddressDict,
)
from .identity_verification_response_user_name import (
    IdentityVerificationResponseUserName,
    IdentityVerificationResponseUserNameDict,
)
from .user_idnumber import UserIdnumber, UserIdnumberDict


class IdentityVerificationAutofillUserData(SdkBaseModel):
    """User information that was autofilled. All this information should be confirmed by the user before using."""

    name: IdentityVerificationResponseUserName | None
    """The full name provided by the user. If the user has not submitted their name, this field will be null. Otherwise,
    both fields are guaranteed to be filled."""

    address: IdentityVerificationAutofillAddress | None
    """Even if an address has been autofilled, some fields may be null depending on the region's addressing system. For
    example:

    Addresses from the United Kingdom will not include a region

    Addresses from Hong Kong will not include postal code"""

    id_number: UserIdnumber | None
    """ID number submitted by the user, currently used only for the Identity Verification product. If the user has not
    submitted this data yet, this field will be ``null``. Otherwise, both fields are guaranteed to be filled."""


class IdentityVerificationAutofillUserDataDict(TypedDict):
    name: IdentityVerificationResponseUserName | IdentityVerificationResponseUserNameDict | None
    address: IdentityVerificationAutofillAddress | IdentityVerificationAutofillAddressDict | None
    id_number: UserIdnumber | UserIdnumberDict | None
