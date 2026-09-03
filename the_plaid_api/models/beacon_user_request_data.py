from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .beacon_user_idnumber import BeaconUserIdnumber, BeaconUserIdnumberDict
from .beacon_user_name import BeaconUserName, BeaconUserNameDict
from .beacon_user_request_address import BeaconUserRequestAddress, BeaconUserRequestAddressDict
from .beacon_user_request_depository_account import (
    BeaconUserRequestDepositoryAccount,
    BeaconUserRequestDepositoryAccountDict,
)


class BeaconUserRequestData(SdkBaseModel):
    """A Beacon User's data which is used to check against duplicate records and the Beacon Fraud Network.

    In order to create a Beacon User, in addition to the ``name``, _either_ the ``date_of_birth`` _or_ the
    ``depository_accounts`` field must be provided."""

    date_of_birth: Optional[Date] = UNSET
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    name: BeaconUserName
    """The full name for a given Beacon User."""

    address: OptionalNullable[BeaconUserRequestAddress] = UNSET
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
    """Provide a list of bank accounts that are associated with this Beacon User. These accounts will be scanned across
    the Beacon Network and used to find duplicate records.

    Note: These accounts will not have Bank Account Insights. To receive Bank Account Insights please supply
    ``access_tokens``."""


class BeaconUserRequestDataDict(TypedDict):
    date_of_birth: NotRequired[Date]
    name: BeaconUserName | BeaconUserNameDict
    address: NotRequired[BeaconUserRequestAddress | BeaconUserRequestAddressDict | None]
    email_address: NotRequired[EmailStr]
    phone_number: NotRequired[str | None]
    id_number: NotRequired[BeaconUserIdnumber | BeaconUserIdnumberDict | None]
    ip_address: NotRequired[str | None]
    depository_accounts: NotRequired[list[BeaconUserRequestDepositoryAccount | BeaconUserRequestDepositoryAccountDict]]
