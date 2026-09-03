from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AddressDataNullable(SdkBaseModel):
    """Data about the components comprising an address."""

    city: str | None
    """The full city name"""

    region: str | None
    """The region or state. In API versions 2018-05-22 and earlier, this field is called ``state``. Example: ``"NC"``"""

    street: str
    """The full street address Example: ``"564 Main Street, APT 15"``"""

    postal_code: str | None
    """The postal code. In API versions 2018-05-22 and earlier, this field is called ``zip``."""

    country: str | None
    """The ISO 3166-1 alpha-2 country code"""


class AddressDataNullableDict(TypedDict):
    city: str | None
    region: str | None
    street: str
    postal_code: str | None
    country: str | None
