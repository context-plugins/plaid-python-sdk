from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraMonitoringInsightsSubscribeResponse(SdkBaseModel):
    """CraMonitoringInsightsSubscribeResponse defines the response schema for ``/cra/monitoring_insights/subscribe``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    subscription_id: str
    """A unique identifier for the subscription."""


class CraMonitoringInsightsSubscribeResponseDict(TypedDict):
    request_id: str
    subscription_id: str
