from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubOverrideEarningsTotal(SdkBaseModel):
    """An object representing both the current pay period and year to date amount for an earning category."""

    hours: OptionalNullable[float] = UNSET
    """Total number of hours worked for this pay period"""

    currency: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the line item"""

    ytd_amount: OptionalNullable[float] = UNSET
    """The year-to-date amount for the total earnings"""


class PaystubOverrideEarningsTotalDict(TypedDict):
    hours: NotRequired[float | None]
    currency: NotRequired[str | None]
    ytd_amount: NotRequired[float | None]
