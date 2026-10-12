from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .address import Address, AddressDict
from .email import Email, EmailDict
from .phone_number import PhoneNumber, PhoneNumberDict


class OwnerOverride(SdkBaseModel):
    """Data about the owner or owners of an account. Any fields not specified will be filled in with default Sandbox
    information."""

    names: list[str]
    """A list of names associated with the account by the financial institution. These should always be the names of
    individuals, even for business accounts. Note that the same name data will be used for all accounts associated with
    an Item."""

    phone_numbers: list[PhoneNumber]
    """A list of phone numbers associated with the account."""

    emails: list[Email]
    """A list of email addresses associated with the account."""

    addresses: list[Address]
    """Data about the various addresses associated with the account."""


class OwnerOverrideDict(TypedDict):
    names: list[str]
    phone_numbers: list[PhoneNumberDict]
    emails: list[EmailDict]
    addresses: list[AddressDict]
