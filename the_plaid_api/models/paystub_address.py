from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubAddress(SdkBaseModel):
    """Address on the paystub"""

    city: OptionalNullable[str] = UNSET
    """The full city name."""

    country: OptionalNullable[str] = UNSET
    """The ISO 3166-1 alpha-2 country code."""

    postal_code: OptionalNullable[str] = UNSET
    """The postal code of the address."""

    region: OptionalNullable[str] = UNSET
    """The region or state Example: ``"NC"``"""

    street: OptionalNullable[str] = UNSET
    """The full street address."""

    line1: OptionalNullable[str] = UNSET
    """Street address line 1."""

    line2: OptionalNullable[str] = UNSET
    """Street address line 2."""

    state_code: OptionalNullable[str] = UNSET
    """The region or state Example: ``"NC"``"""


class PaystubAddressDict(TypedDict):
    city: NotRequired[str | None]
    country: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    region: NotRequired[str | None]
    street: NotRequired[str | None]
    line1: NotRequired[str | None]
    line2: NotRequired[str | None]
    state_code: NotRequired[str | None]
