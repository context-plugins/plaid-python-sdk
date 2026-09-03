from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.network_insights_version import NetworkInsightsVersionOrStr


class CraCheckReportNetworkInsightsGetOptions(SdkBaseModel):
    """Deprecated. This field is no longer accepted for new clients (created on or after 2026-07-01). New clients should
    specify required products when creating the Consumer Report. Existing integrations may continue to pass
    ``options``."""

    network_insights_version: OptionalNullable[NetworkInsightsVersionOrStr] = UNSET
    """The version of Network Insights. Required if using Network Insights."""


class CraCheckReportNetworkInsightsGetOptionsDict(TypedDict):
    network_insights_version: NotRequired[NetworkInsightsVersionOrStr | None]
