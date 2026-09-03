from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.monitoring_item_status_code import MonitoringItemStatusCodeOrStr


class MonitoringInsightsItemStatus(SdkBaseModel):
    """An object with details of the Monitoring Insights Item's status."""

    status_code: MonitoringItemStatusCodeOrStr
    """Enum for the status of the Item's insights"""

    reason: OptionalNullable[str] = UNSET
    """A reason for why a Monitoring Insights Report is not available. This field will only be populated when the
    ``status_code`` is not ``AVAILABLE``"""


class MonitoringInsightsItemStatusDict(TypedDict):
    status_code: MonitoringItemStatusCodeOrStr
    reason: NotRequired[str | None]
