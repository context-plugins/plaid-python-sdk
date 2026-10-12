from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .address import Address, AddressDict
from .email import Email, EmailDict
from .phone_number import PhoneNumber, PhoneNumberDict


class Owner(SdkBaseModel):
    """Data returned from the financial institution about the owner or owners of an account. Only the ``names`` array
    must be non-empty."""

    names: list[str]
    """A list of names associated with the account by the financial institution. In the case of a joint account, Plaid
    will make a best effort to report the names of all account holders.

    If an Item contains multiple accounts with different owner names, some institutions will report all names associated
    with the Item in each account's ``names`` array."""

    phone_numbers: list[PhoneNumber]
    """A list of phone numbers associated with the account by the financial institution. May be an empty array if no
    relevant information is returned from the financial institution."""

    emails: list[Email]
    """A list of email addresses associated with the account by the financial institution. May be an empty array if no
    relevant information is returned from the financial institution."""

    addresses: list[Address]
    """Data about the various addresses associated with the account by the financial institution. May be an empty array
    if no relevant information is returned from the financial institution."""


class OwnerDict(TypedDict):
    names: list[str]
    phone_numbers: list[PhoneNumberDict]
    emails: list[EmailDict]
    addresses: list[AddressDict]
