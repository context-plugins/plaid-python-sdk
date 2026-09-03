from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.refresh_interval import RefreshIntervalOrStr


class StatusBreakdown(SdkBaseModel):
    """A detailed breakdown of the institution's performance for a request type. The values for ``success``,
    ``error_plaid``, and ``error_institution`` sum to 1. The time range used for calculating the breakdown may range
    from the most recent few minutes to the past six hours. In general, smaller institutions will show status that was
    calculated over a longer period of time. For Investment updates, which are refreshed less frequently, the period
    assessed may be 24 hours or more. For more details, see `Institution status details
    <https://plaid.com/docs/account/activity/#troubleshooting-institution-insights>`__."""

    success: float
    """The percentage of login attempts that are successful, expressed as a decimal."""

    error_plaid: float
    """The percentage of logins that are failing due to an internal Plaid issue, expressed as a decimal."""

    error_institution: float
    """The percentage of logins that are failing due to an issue in the institution's system, expressed as a decimal."""

    refresh_interval: Optional[RefreshIntervalOrStr] = UNSET
    """How frequently data for subscription products like Investments, Transactions, and Liabilities, is being
    refreshed, relative to the institution's normal scheduling. The ``refresh_interval`` may be ``DELAYED`` or
    ``STOPPED`` even when the success rate is high."""


class StatusBreakdownDict(TypedDict):
    success: float
    error_plaid: float
    error_institution: float
    refresh_interval: NotRequired[RefreshIntervalOrStr]
