from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IncomeVerificationPrecheckEmployerAddress(SdkBaseModel):
    """The address of the employer"""

    city: Optional[str] = UNSET
    """The full city name"""

    country: Optional[str] = UNSET
    """The ISO 3166-1 alpha-2 country code"""

    postal_code: Optional[str] = UNSET
    """The postal code. In API versions 2018-05-22 and earlier, this field is called ``zip``."""

    region: Optional[str] = UNSET
    """The region or state. In API versions 2018-05-22 and earlier, this field is called ``state``. Example: ``"NC"``"""

    street: Optional[str] = UNSET
    """The full street address Example: ``"564 Main Street, APT 15"``"""


class IncomeVerificationPrecheckEmployerAddressDict(TypedDict):
    city: NotRequired[str]
    country: NotRequired[str]
    postal_code: NotRequired[str]
    region: NotRequired[str]
    street: NotRequired[str]
