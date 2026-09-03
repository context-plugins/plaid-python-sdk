from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResponseBusinessAddress(SdkBaseModel):
    """Physical address of a business. Used for response schemas."""

    street: str | None
    """The primary street portion of an address. If an address is provided, this field will always be filled. A string
    with at least one non-whitespace alphabetical character, with a max length of 80 characters."""

    street2: str | None
    """Extra street information, like an apartment or suite number. If provided, a string with at least one
    non-whitespace character, with a max length of 50 characters."""

    city: str | None
    """City from the address. A string with at least one non-whitespace alphabetical character, with a max length of 100
    characters."""

    region: str | None
    """A subdivision code. "Subdivision" is a generic term for "state", "province", "prefecture", "zone", etc. For the
    list of valid codes, see `country subdivision codes <https://plaid.com/documents/country_subdivision_codes.json>`__.
    Country prefixes are omitted, since they are inferred from the ``country`` field."""

    postal_code: str | None
    """The postal code for the associated address. Between 2 and 10 alphanumeric characters. For US-based addresses this
    must be 5 numeric digits."""

    country: str
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""


class ResponseBusinessAddressDict(TypedDict):
    street: str | None
    street2: str | None
    city: str | None
    region: str | None
    postal_code: str | None
    country: str
