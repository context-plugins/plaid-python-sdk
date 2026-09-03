from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .beacon_user_address import BeaconUserAddress, BeaconUserAddressDict
from .beacon_user_depository_account import BeaconUserDepositoryAccount, BeaconUserDepositoryAccountDict
from .beacon_user_idnumber import BeaconUserIdnumber, BeaconUserIdnumberDict
from .beacon_user_name import BeaconUserName, BeaconUserNameDict


class BeaconUserData(SdkBaseModel):
    """A Beacon User's data and resulting analysis when checked against duplicate records and the Beacon Fraud
    Network."""

    date_of_birth: Date
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    name: BeaconUserName
    """The full name for a given Beacon User."""

    address: BeaconUserAddress
    """Even if an address has been collected, some fields may be null depending on the region's addressing system. For
    example:


    Addresses from the United Kingdom will not include a region


    Addresses from Hong Kong will not include a postal code"""

    email_address: EmailStr | None
    """A valid email address. Must not have leading or trailing spaces and address must be RFC compliant. For more
    information, see `RFC 3696 <https://datatracker.ietf.org/doc/html/rfc3696>`__."""

    phone_number: str | None
    """A phone number in E.164 format."""

    id_number: BeaconUserIdnumber | None
    """The ID number associated with a Beacon User."""

    ip_address: str | None
    """An IPv4 or IPv6 address."""

    depository_accounts: list[BeaconUserDepositoryAccount]


class BeaconUserDataDict(TypedDict):
    date_of_birth: Date
    name: BeaconUserName | BeaconUserNameDict
    address: BeaconUserAddress | BeaconUserAddressDict
    email_address: EmailStr | None
    phone_number: str | None
    id_number: BeaconUserIdnumber | BeaconUserIdnumberDict | None
    ip_address: str | None
    depository_accounts: list[BeaconUserDepositoryAccount | BeaconUserDepositoryAccountDict]
