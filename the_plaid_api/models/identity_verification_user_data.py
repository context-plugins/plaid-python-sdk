from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .identity_verification_response_user_name import (
    IdentityVerificationResponseUserName,
    IdentityVerificationResponseUserNameDict,
)
from .identity_verification_user_address import IdentityVerificationUserAddress, IdentityVerificationUserAddressDict
from .user_idnumber import UserIdnumber, UserIdnumberDict


class IdentityVerificationUserData(SdkBaseModel):
    """The identity data that was either collected from the user or provided via API in order to perform an Identity
    Verification."""

    phone_number: OptionalNullable[str] = UNSET
    """A valid phone number in E.164 format."""

    date_of_birth: Date | None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    ip_address: str | None
    """An IPv4 or IPv6 address."""

    email_address: EmailStr | None
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""

    name: IdentityVerificationResponseUserName | None
    """The full name provided by the user. If the user has not submitted their name, this field will be null. Otherwise,
    both fields are guaranteed to be filled."""

    address: IdentityVerificationUserAddress | None
    """Even if an address has been collected, some fields may be null depending on the region's addressing system. For
    example:

    Addresses from the United Kingdom will not include a region

    Addresses from Hong Kong will not include postal code"""

    id_number: UserIdnumber | None
    """ID number submitted by the user, currently used only for the Identity Verification product. If the user has not
    submitted this data yet, this field will be ``null``. Otherwise, both fields are guaranteed to be filled."""


class IdentityVerificationUserDataDict(TypedDict):
    phone_number: NotRequired[str | None]
    date_of_birth: Date | None
    ip_address: str | None
    email_address: EmailStr | None
    name: IdentityVerificationResponseUserName | IdentityVerificationResponseUserNameDict | None
    address: IdentityVerificationUserAddress | IdentityVerificationUserAddressDict | None
    id_number: UserIdnumber | UserIdnumberDict | None
