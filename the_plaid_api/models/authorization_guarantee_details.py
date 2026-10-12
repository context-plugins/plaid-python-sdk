from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .authorization_guarantee_schedule_item import (
    AuthorizationGuaranteeScheduleItem,
    AuthorizationGuaranteeScheduleItemDict,
)
from .enums.transfer_guarantee_outcome import TransferGuaranteeOutcomeOrStr


class AuthorizationGuaranteeDetails(SdkBaseModel):
    """Adaptive guarantee details for a transfer authorization, including the guarantee outcome and settlement schedule.
    Omitted when no guarantee was attempted."""

    outcome: TransferGuaranteeOutcomeOrStr
    """The adaptive guarantee outcome for a transfer.

    ``FULL_INSTANT``: The full transfer amount is guaranteed and funds are available instantly.

    ``PARTIAL_INSTANT_ONLY``: A partial amount is guaranteed and available instantly; the remainder is not guaranteed.

    ``PARTIAL_INSTANT_WITH_OBSERVATION_WINDOW``: A partial amount is guaranteed instantly; an additional amount is
    conditionally guaranteed subject to an observation window.

    ``NOT_GUARANTEED``: Plaid did not provide a guarantee for this transfer."""

    schedule: list[AuthorizationGuaranteeScheduleItem]
    """The adaptive guarantee settlement schedule for this authorization."""


class AuthorizationGuaranteeDetailsDict(TypedDict):
    outcome: TransferGuaranteeOutcomeOrStr
    schedule: list[AuthorizationGuaranteeScheduleItemDict]
