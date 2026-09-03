from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.network_insights_version import NetworkInsightsVersionOrStr


class CraCheckReportCreateNetworkInsightsOptions(SdkBaseModel):
    """Defines configuration options to generate Network Insights"""

    network_insights_version: OptionalNullable[NetworkInsightsVersionOrStr] = UNSET
    """The version of Network Insights. Required if using Network Insights."""


class CraCheckReportCreateNetworkInsightsOptionsDict(TypedDict):
    network_insights_version: NotRequired[NetworkInsightsVersionOrStr | None]
