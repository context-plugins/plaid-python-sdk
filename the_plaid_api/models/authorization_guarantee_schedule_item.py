from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuthorizationGuaranteeScheduleItem(SdkBaseModel):
    """A single entry in an authorization's adaptive guarantee settlement schedule, describing one tranche of guaranteed
    funds."""

    amount: str
    """The guaranteed amount for this schedule entry (decimal string with two digits of precision e.g. "10.00")."""

    observation_window_business_days: int
    """The number of business days in the observation window for this tranche. ``0`` when the tranche is not subject to
    an observation window."""


class AuthorizationGuaranteeScheduleItemDict(TypedDict):
    amount: str
    observation_window_business_days: int
