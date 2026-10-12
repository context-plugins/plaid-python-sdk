from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .beacon_user_idnumber import BeaconUserIdnumber, BeaconUserIdnumberDict
from .beacon_user_name_nullable import BeaconUserNameNullable, BeaconUserNameNullableDict
from .beacon_user_request_address_nullable import BeaconUserRequestAddressNullable, BeaconUserRequestAddressNullableDict
from .beacon_user_request_depository_account import (
    BeaconUserRequestDepositoryAccount,
    BeaconUserRequestDepositoryAccountDict,
)


class BeaconUserUpdateRequestData(SdkBaseModel):
    """A subset of a Beacon User's data which is used to patch the existing identity data associated with a Beacon User.
    At least one field must be provided. If left unset or null, user data will not be patched."""

    date_of_birth: Optional[Date] = UNSET
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    name: OptionalNullable[BeaconUserNameNullable] = UNSET
    """The full name for a given Beacon User."""

    address: OptionalNullable[BeaconUserRequestAddressNullable] = UNSET
    """Home address for the associated user. For more context on this field, see `Input Validation by Country
    <https://plaid.com/docs/identity-verification/hybrid-input-validation/#input-validation-by-country>`__."""

    email_address: Optional[EmailStr] = UNSET
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""

    phone_number: OptionalNullable[str] = UNSET
    """A phone number in E.164 format."""

    id_number: OptionalNullable[BeaconUserIdnumber] = UNSET
    """The ID number associated with a Beacon User."""

    ip_address: OptionalNullable[str] = UNSET
    """An IPv4 or IPv6 address."""

    depository_accounts: Optional[list[BeaconUserRequestDepositoryAccount]] = UNSET


class BeaconUserUpdateRequestDataDict(TypedDict):
    date_of_birth: NotRequired[Date]
    name: NotRequired[BeaconUserNameNullableDict | None]
    address: NotRequired[BeaconUserRequestAddressNullableDict | None]
    email_address: NotRequired[EmailStr]
    phone_number: NotRequired[str | None]
    id_number: NotRequired[BeaconUserIdnumberDict | None]
    ip_address: NotRequired[str | None]
    depository_accounts: NotRequired[list[BeaconUserRequestDepositoryAccountDict]]
