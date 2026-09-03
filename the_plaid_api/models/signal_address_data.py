from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SignalAddressData(SdkBaseModel):
    """Data about the components comprising an address."""

    city: Optional[str] = UNSET
    """The full city name"""

    region: OptionalNullable[str] = UNSET
    """The region or state Example: ``"NC"``"""

    street: Optional[str] = UNSET
    """The full street address Example: ``"564 Main Street, APT 15"``"""

    postal_code: OptionalNullable[str] = UNSET
    """The postal code"""

    country: OptionalNullable[str] = UNSET
    """The ISO 3166-1 alpha-2 country code"""


class SignalAddressDataDict(TypedDict):
    city: NotRequired[str]
    region: NotRequired[str | None]
    street: NotRequired[str]
    postal_code: NotRequired[str | None]
    country: NotRequired[str | None]
