from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubOverrideDeductionsBreakdown(SdkBaseModel):
    """An object representing the deduction line items for the pay period"""

    current_amount: OptionalNullable[float] = UNSET
    """Raw amount of the deduction"""

    description: OptionalNullable[str] = UNSET
    """Description of the deduction line item"""

    currency: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the line item."""

    ytd_amount: OptionalNullable[float] = UNSET
    """The year-to-date amount of the deduction"""


class PaystubOverrideDeductionsBreakdownDict(TypedDict):
    current_amount: NotRequired[float | None]
    description: NotRequired[str | None]
    currency: NotRequired[str | None]
    ytd_amount: NotRequired[float | None]
