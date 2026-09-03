from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .enums.paystub_pay_frequency import PaystubPayFrequencyOrStr


class PaystubDetails(SdkBaseModel):
    """An object representing details that can be found on the paystub."""

    pay_period_start_date: OptionalNullable[Date] = UNSET
    """Beginning date of the pay period on the paystub in the 'YYYY-MM-DD' format."""

    pay_period_end_date: OptionalNullable[Date] = UNSET
    """Ending date of the pay period on the paystub in the 'YYYY-MM-DD' format."""

    pay_date: OptionalNullable[Date] = UNSET
    """Pay date on the paystub in the 'YYYY-MM-DD' format."""

    paystub_provider: OptionalNullable[str] = UNSET
    """The name of the payroll provider that generated the paystub, e.g. ADP"""

    pay_frequency: OptionalNullable[PaystubPayFrequencyOrStr] = UNSET
    """The frequency at which the employee is paid. Possible values: ``MONTHLY``, ``BI-WEEKLY``, ``WEEKLY``,
    ``SEMI-MONTHLY``."""


class PaystubDetailsDict(TypedDict):
    pay_period_start_date: NotRequired[Date | None]
    pay_period_end_date: NotRequired[Date | None]
    pay_date: NotRequired[Date | None]
    paystub_provider: NotRequired[str | None]
    pay_frequency: NotRequired[PaystubPayFrequencyOrStr | None]
