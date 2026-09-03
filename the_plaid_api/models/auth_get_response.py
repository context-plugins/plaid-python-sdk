from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account import Account, AccountDict
from .auth_get_numbers import AuthGetNumbers, AuthGetNumbersDict
from .item import Item, ItemDict


class AuthGetResponse(SdkBaseModel):
    """AuthGetResponse defines the response schema for ``/auth/get``"""

    accounts: list[Account]
    """The ``accounts`` for which numbers are being retrieved."""

    numbers: AuthGetNumbers
    """An object containing identifying numbers used for making electronic transfers to and from the ``accounts``. The
    identifying number type (ACH, EFT, IBAN, or Bacs) used will depend on the country of the account. An account may
    have more than one number type. If a particular identifying number type is not used by any ``accounts`` for which
    data has been requested, the array for that type will be empty."""

    item: Item
    """Metadata about the Item."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class AuthGetResponseDict(TypedDict):
    accounts: list[Account | AccountDict]
    numbers: AuthGetNumbers | AuthGetNumbersDict
    item: Item | ItemDict
    request_id: str
