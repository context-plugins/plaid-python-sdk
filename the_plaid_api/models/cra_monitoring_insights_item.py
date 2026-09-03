from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .base_report_account import BaseReportAccount, BaseReportAccountDict
from .monitoring_insights import MonitoringInsights, MonitoringInsightsDict
from .monitoring_insights_item_status import MonitoringInsightsItemStatus, MonitoringInsightsItemStatusDict


class CraMonitoringInsightsItem(SdkBaseModel):
    """An object representing a Monitoring Insights Item"""

    date_generated: RFC3339DateTime
    """The date and time when the specific insights were generated (per-item), in `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (e.g. "2018-04-12T03:32:11Z")."""

    item_id: str
    """The ``item_id`` of the Item associated with the insights"""

    institution_id: str
    """The id of the financial institution associated with the Item."""

    institution_name: str
    """The full financial institution name associated with the Item."""

    status: MonitoringInsightsItemStatus
    """An object with details of the Monitoring Insights Item's status."""

    insights: MonitoringInsights | None
    """An object representing the Monitoring Insights for the given Item"""

    accounts: Optional[list[BaseReportAccount]] = UNSET
    """Data about each of the accounts open on the Item."""


class CraMonitoringInsightsItemDict(TypedDict):
    date_generated: RFC3339DateTime
    item_id: str
    institution_id: str
    institution_name: str
    status: MonitoringInsightsItemStatus | MonitoringInsightsItemStatusDict
    insights: MonitoringInsights | MonitoringInsightsDict | None
    accounts: NotRequired[list[BaseReportAccount | BaseReportAccountDict]]
