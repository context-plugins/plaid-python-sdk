from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.pay_period_details_pay_frequency import PayPeriodDetailsPayFrequencyOrStr
from .paystub_override_distribution_breakdown import (
    PaystubOverrideDistributionBreakdown,
    PaystubOverrideDistributionBreakdownDict,
)


class PaystubOverridePayPeriodDetails(SdkBaseModel):
    """Details about the pay period."""

    check_amount: OptionalNullable[float] = UNSET
    """The amount of the paycheck."""

    distribution_breakdown: Optional[list[PaystubOverrideDistributionBreakdown]] = UNSET
    end_date: OptionalNullable[Date] = UNSET
    """The pay period end date, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format: "yyyy-mm-dd"."""

    gross_earnings: OptionalNullable[float] = UNSET
    """Total earnings before tax/deductions."""

    pay_date: OptionalNullable[Date] = UNSET
    """The date on which the paystub was issued, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""

    pay_frequency: OptionalNullable[PayPeriodDetailsPayFrequencyOrStr] = UNSET
    """The frequency at which an individual is paid."""

    pay_day: OptionalNullable[Date] = UNSET
    """The date on which the paystub was issued, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    ("yyyy-mm-dd")."""

    start_date: OptionalNullable[Date] = UNSET
    """The pay period start date, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format: "yyyy-mm-dd"."""


class PaystubOverridePayPeriodDetailsDict(TypedDict):
    check_amount: NotRequired[float | None]
    distribution_breakdown: NotRequired[
        list[PaystubOverrideDistributionBreakdown | PaystubOverrideDistributionBreakdownDict]
    ]
    end_date: NotRequired[Date | None]
    gross_earnings: NotRequired[float | None]
    pay_date: NotRequired[Date | None]
    pay_frequency: NotRequired[PayPeriodDetailsPayFrequencyOrStr | None]
    pay_day: NotRequired[Date | None]
    start_date: NotRequired[Date | None]
