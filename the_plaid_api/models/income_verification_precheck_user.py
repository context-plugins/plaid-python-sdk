from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .signal_address_data import SignalAddressData, SignalAddressDataDict


class IncomeVerificationPrecheckUser(SdkBaseModel):
    """Information about the user whose eligibility is being evaluated."""

    first_name: OptionalNullable[str] = UNSET
    """The user's first name"""

    last_name: OptionalNullable[str] = UNSET
    """The user's last name"""

    email_address: OptionalNullable[str] = UNSET
    """The user's email address"""

    home_address: OptionalNullable[SignalAddressData] = UNSET
    """Data about the components comprising an address."""


class IncomeVerificationPrecheckUserDict(TypedDict):
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    email_address: NotRequired[str | None]
    home_address: NotRequired[SignalAddressDataDict | None]
