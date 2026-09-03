from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.payment_schedule_interval import PaymentScheduleIntervalOrStr


class PaymentInitiationStandingOrderMetadata(SdkBaseModel):
    """Metadata specifically related to valid Payment Initiation standing order configurations for the institution."""

    supports_standing_order_end_date: bool
    """Indicates whether the institution supports closed-ended standing orders by providing an end date."""

    supports_standing_order_negative_execution_days: bool
    """This is only applicable to ``MONTHLY`` standing orders. Indicates whether the institution supports negative
    integers (-1 to -5) for setting up a ``MONTHLY`` standing order relative to the end of the month."""

    valid_standing_order_intervals: list[PaymentScheduleIntervalOrStr]
    """A list of the valid standing order intervals supported by the institution."""


class PaymentInitiationStandingOrderMetadataDict(TypedDict):
    supports_standing_order_end_date: bool
    supports_standing_order_negative_execution_days: bool
    valid_standing_order_intervals: list[PaymentScheduleIntervalOrStr]
