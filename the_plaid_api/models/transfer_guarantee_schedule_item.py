from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel


class TransferGuaranteeScheduleItem(SdkBaseModel):
    """A single entry in the adaptive guarantee settlement schedule, describing one tranche of guaranteed funds. Adds
    ``observation_window_expiration_time``, which is only known once a transfer is created."""

    amount: str
    """The guaranteed amount for this schedule entry (decimal string with two digits of precision e.g. "10.00")."""

    observation_window_business_days: int
    """The number of business days in the observation window for this tranche. ``0`` when the tranche is not subject to
    an observation window."""

    observation_window_expiration_time: OptionalNullable[RFC3339DateTime] = UNSET
    """The datetime when the observation window for this tranche expires. Present only when the tranche is subject to an
    observation window. This will be of the form ``2006-01-02T15:04:05Z``."""


class TransferGuaranteeScheduleItemDict(TypedDict):
    amount: str
    observation_window_business_days: int
    observation_window_expiration_time: NotRequired[RFC3339DateTime | None]
