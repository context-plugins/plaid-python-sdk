from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferPlatformPersonAddress(SdkBaseModel):
    """Home address of a person"""

    city: str
    """The full city name."""

    country: str
    """Valid, capitalized, two-letter ISO code representing the country of this object. Must be in ISO 3166-1 alpha-2
    form."""

    postal_code: str
    """The postal code of the address."""

    region: str
    """An ISO 3166-2 subdivision code. Related terms would be "state", "province", "prefecture", "zone", "subdivision",
    etc."""

    street: str
    """The primary street portion of an address. A string with at least one non-whitespace alphabetical character, with
    a max length of 80 characters."""

    street2: Optional[str] = UNSET
    """Extra street information, like an apartment or suite number. If provided, a string with at least one
    non-whitespace character, with a max length of 50 characters."""


class TransferPlatformPersonAddressDict(TypedDict):
    city: str
    country: str
    postal_code: str
    region: str
    street: str
    street2: NotRequired[str]
