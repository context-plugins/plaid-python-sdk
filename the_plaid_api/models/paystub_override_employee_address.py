from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaystubOverrideEmployeeAddress(SdkBaseModel):
    """The address of the employee."""

    city: Optional[str] = UNSET
    """The full city name."""

    region: Optional[str] = UNSET
    """The region or state Example: ``"NC"``"""

    street: Optional[str] = UNSET
    """The full street address Example: ``"564 Main Street, APT 15"``"""

    postal_code: Optional[str] = UNSET
    """5 digit postal code."""

    country: Optional[str] = UNSET
    """The country of the address."""


class PaystubOverrideEmployeeAddressDict(TypedDict):
    city: NotRequired[str]
    region: NotRequired[str]
    street: NotRequired[str]
    postal_code: NotRequired[str]
    country: NotRequired[str]
