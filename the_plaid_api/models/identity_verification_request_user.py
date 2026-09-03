from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .identity_verification_request_user_name import (
    IdentityVerificationRequestUserName,
    IdentityVerificationRequestUserNameDict,
)
from .user_address import UserAddress, UserAddressDict
from .user_idnumber import UserIdnumber, UserIdnumberDict


class IdentityVerificationRequestUser(SdkBaseModel):
    """User information collected outside of Link, most likely via your own onboarding process.

    Each of the following identity fields are optional:

    ``email_address``

    ``phone_number``

    ``date_of_birth``

    ``name``

    ``address``

    ``id_number``

    Specifically, these fields are optional in that they can either be fully provided (satisfying every required field
    in their subschema) or omitted from the request entirely by not providing the key or value. Providing these fields
    via the API will result in Link skipping the data collection process for the associated user. All verification steps
    enabled in the associated Identity Verification Template will still be run. Verification steps will either be run
    immediately, or once the user completes the ``accept_tos`` step, depending on the value provided to the
    ``gave_consent`` field."""

    email_address: Optional[EmailStr] = UNSET
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""

    phone_number: OptionalNullable[str] = UNSET
    """A valid phone number in E.164 format."""

    date_of_birth: Optional[Date] = UNSET
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    name: OptionalNullable[IdentityVerificationRequestUserName] = UNSET
    """You can use this field to pre-populate the user's legal name; if it is provided here, they will not be prompted
    to enter their name in the identity verification attempt."""

    address: OptionalNullable[UserAddress] = UNSET
    """Home address for the user. Supported values are: not provided, address with only country code or full address.

    For more context on this field, see `Input Validation by Country
    <https://plaid.com/docs/identity-verification/hybrid-input-validation/#input-validation-by-country>`__."""

    id_number: OptionalNullable[UserIdnumber] = UNSET
    """ID number submitted by the user, currently used only for the Identity Verification product. If the user has not
    submitted this data yet, this field will be ``null``. Otherwise, both fields are guaranteed to be filled."""


class IdentityVerificationRequestUserDict(TypedDict):
    email_address: NotRequired[EmailStr]
    phone_number: NotRequired[str | None]
    date_of_birth: NotRequired[Date]
    name: NotRequired[IdentityVerificationRequestUserName | IdentityVerificationRequestUserNameDict | None]
    address: NotRequired[UserAddress | UserAddressDict | None]
    id_number: NotRequired[UserIdnumber | UserIdnumberDict | None]
