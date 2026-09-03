from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubOverrideDeductionsTotal(SdkBaseModel):
    """An object representing the total deductions for the pay period"""

    current_amount: OptionalNullable[float] = UNSET
    """Raw amount of the deduction"""

    currency: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the line item."""

    ytd_amount: OptionalNullable[float] = UNSET
    """The year-to-date total amount of the deductions"""


class PaystubOverrideDeductionsTotalDict(TypedDict):
    current_amount: NotRequired[float | None]
    currency: NotRequired[str | None]
    ytd_amount: NotRequired[float | None]
