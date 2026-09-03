from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .cra_network_insights_item import CraNetworkInsightsItem, CraNetworkInsightsItemDict


class CraNetworkInsightsReport(SdkBaseModel):
    """Contains data for the CRA Network Attributes Report."""

    report_id: str
    """The unique identifier associated with the report object."""

    generated_time: RFC3339DateTime
    """The time when the report was generated."""

    network_attributes: Any
    """A map of network attributes, where the key is a string, and the value is a float, int, or boolean. For a full
    list of attributes, contact your account manager."""

    items: list[CraNetworkInsightsItem]
    """The Items the end user connected in Link."""


class CraNetworkInsightsReportDict(TypedDict):
    report_id: str
    generated_time: RFC3339DateTime
    network_attributes: Any
    items: list[CraNetworkInsightsItem | CraNetworkInsightsItemDict]
