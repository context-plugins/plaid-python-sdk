from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .transfer_guarantee_schedule_item import TransferGuaranteeScheduleItem, TransferGuaranteeScheduleItemDict


class TransferGuaranteeDetails(SdkBaseModel):
    """Adaptive guarantee details for a transfer, including the guaranteed amount and settlement schedule. Omitted when
    no guarantee was attempted."""

    guaranteed_amount: str
    """The amount currently covered by Plaid's guarantee (decimal string with two digits of precision e.g. "10.00").
    This may change over time as scheduled tranches reach their observation window expiration and become guaranteed."""

    schedule: list[TransferGuaranteeScheduleItem]
    """The adaptive guarantee settlement schedule for this transfer."""


class TransferGuaranteeDetailsDict(TypedDict):
    guaranteed_amount: str
    schedule: list[TransferGuaranteeScheduleItem | TransferGuaranteeScheduleItemDict]
