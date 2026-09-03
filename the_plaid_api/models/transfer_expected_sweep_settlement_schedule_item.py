from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel


class TransferExpectedSweepSettlementScheduleItem(SdkBaseModel):
    """Defines an expected sweep date and amount."""

    sweep_settlement_date: Date
    """The settlement date of a sweep for this transfer."""

    swept_settled_amount: str
    """The accumulated amount that has been swept by ``sweep_settlement_date``."""


class TransferExpectedSweepSettlementScheduleItemDict(TypedDict):
    sweep_settlement_date: Date
    swept_settled_amount: str
