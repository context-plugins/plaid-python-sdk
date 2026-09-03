from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubOverrideNetPay(SdkBaseModel):
    """An object representing information about the net pay amount on the paystub."""

    description: OptionalNullable[str] = UNSET
    """Description of the net pay"""

    currency: OptionalNullable[str] = UNSET
    """The ISO-4217 currency code of the net pay."""

    ytd_amount: OptionalNullable[float] = UNSET
    """The year-to-date amount of the net pay"""


class PaystubOverrideNetPayDict(TypedDict):
    description: NotRequired[str | None]
    currency: NotRequired[str | None]
    ytd_amount: NotRequired[float | None]
