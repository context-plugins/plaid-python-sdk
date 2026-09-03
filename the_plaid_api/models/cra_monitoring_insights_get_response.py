from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_monitoring_insights_item import CraMonitoringInsightsItem, CraMonitoringInsightsItemDict


class CraMonitoringInsightsGetResponse(SdkBaseModel):
    """CraMonitoringInsightsGetResponse defines the response schema for ``/cra/monitoring_insights/get``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    user_insights_id: str
    """A unique ID identifying a User Monitoring Insights Report. Like all Plaid identifiers, this ID is case
    sensitive."""

    items: list[CraMonitoringInsightsItem]
    """An array of Monitoring Insights Items associated with the user."""


class CraMonitoringInsightsGetResponseDict(TypedDict):
    request_id: str
    user_insights_id: str
    items: list[CraMonitoringInsightsItem | CraMonitoringInsightsItemDict]
