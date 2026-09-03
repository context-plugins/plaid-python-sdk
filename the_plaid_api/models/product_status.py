from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.status4 import Status4OrStr
from .status_breakdown import StatusBreakdown, StatusBreakdownDict


class ProductStatus(SdkBaseModel):
    """A representation of the status health of a request type. Auth requests, Balance requests, Identity requests,
    Investments requests, Liabilities requests, Transactions updates, Investments updates, Liabilities updates, and Item
    logins each have their own status object."""

    status: Status4OrStr
    """This field is deprecated in favor of the ``breakdown`` object, which provides more granular institution health
    data.

    ``HEALTHY``: the majority of requests are successful ``DEGRADED``: only some requests are successful ``DOWN``: all
    requests are failing"""

    last_status_change: RFC3339DateTime
    """`ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ formatted timestamp of the last status change for the
    institution."""

    breakdown: StatusBreakdown
    """A detailed breakdown of the institution's performance for a request type. The values for ``success``,
    ``error_plaid``, and ``error_institution`` sum to 1. The time range used for calculating the breakdown may range
    from the most recent few minutes to the past six hours. In general, smaller institutions will show status that was
    calculated over a longer period of time. For Investment updates, which are refreshed less frequently, the period
    assessed may be 24 hours or more. For more details, see `Institution status details
    <https://plaid.com/docs/account/activity/#troubleshooting-institution-insights>`__."""


class ProductStatusDict(TypedDict):
    status: Status4OrStr
    last_status_change: RFC3339DateTime
    breakdown: StatusBreakdown | StatusBreakdownDict
