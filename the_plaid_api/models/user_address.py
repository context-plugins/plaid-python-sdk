from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UserAddress(SdkBaseModel):
    """Home address for the user. Supported values are: not provided, address with only country code or full address.

    For more context on this field, see `Input Validation by Country
    <https://plaid.com/docs/identity-verification/hybrid-input-validation/#input-validation-by-country>`__."""

    street: OptionalNullable[str] = UNSET
    """The primary street portion of an address. If an address is provided, this field will always be filled. A string
    with at least one non-whitespace alphabetical character, with a max length of 80 characters."""

    street2: OptionalNullable[str] = UNSET
    """Extra street information, like an apartment or suite number. If provided, a string with at least one
    non-whitespace character, with a max length of 50 characters."""

    city: OptionalNullable[str] = UNSET
    """City from the address. A string with at least one non-whitespace alphabetical character, with a max length of 100
    characters."""

    region: OptionalNullable[str] = UNSET
    """A subdivision code. "Subdivision" is a generic term for "state", "province", "prefecture", "zone", etc. For the
    list of valid codes, see `country subdivision codes <https://plaid.com/documents/country_subdivision_codes.json>`__.
    Country prefixes are omitted, since they are inferred from the ``country`` field."""

    postal_code: OptionalNullable[str] = UNSET
    """The postal code for the associated address. Between 2 and 10 alphanumeric characters. For US-based addresses this
    must be 5 numeric digits."""

    country: str
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""


class UserAddressDict(TypedDict):
    street: NotRequired[str | None]
    street2: NotRequired[str | None]
    city: NotRequired[str | None]
    region: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    country: str
