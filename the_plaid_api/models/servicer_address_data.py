from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ServicerAddressData(SdkBaseModel):
    """The address of the student loan servicer. This is generally the remittance address to which payments should be
    sent."""

    city: str | None
    """The full city name"""

    region: str | None
    """The region or state Example: ``"NC"``"""

    street: str | None
    """The full street address Example: ``"564 Main Street, APT 15"``"""

    postal_code: str | None
    """The postal code"""

    country: str | None
    """The ISO 3166-1 alpha-2 country code"""


class ServicerAddressDataDict(TypedDict):
    city: str | None
    region: str | None
    street: str | None
    postal_code: str | None
    country: str | None
