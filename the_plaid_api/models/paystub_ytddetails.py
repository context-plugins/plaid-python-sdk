from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaystubYtddetails(SdkBaseModel):
    """The amount of income earned year to date, as based on paystub data."""

    gross_earnings: OptionalNullable[float] = UNSET
    """Year-to-date gross earnings."""

    net_earnings: OptionalNullable[float] = UNSET
    """Year-to-date net (take home) earnings."""


class PaystubYtddetailsDict(TypedDict):
    gross_earnings: NotRequired[float | None]
    net_earnings: NotRequired[float | None]
