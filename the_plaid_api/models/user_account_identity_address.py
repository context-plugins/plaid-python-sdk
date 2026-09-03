from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UserAccountIdentityAddress(SdkBaseModel):
    """The user's address."""

    city: OptionalNullable[str] = UNSET
    """The full city name"""

    region: OptionalNullable[str] = UNSET
    """The region or state. Example: ``"NC"``"""

    street: OptionalNullable[str] = UNSET
    """The full street address Example: ``"564 Main Street, APT 15"``"""

    street2: OptionalNullable[str] = UNSET
    """The second line street address"""

    postal_code: OptionalNullable[str] = UNSET
    """The postal code. In API versions 2018-05-22 and earlier, this field is called ``zip``."""

    country: OptionalNullable[str] = UNSET
    """The ISO 3166-1 alpha-2 country code"""


class UserAccountIdentityAddressDict(TypedDict):
    city: NotRequired[str | None]
    region: NotRequired[str | None]
    street: NotRequired[str | None]
    street2: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    country: NotRequired[str | None]
