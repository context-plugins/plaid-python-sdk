from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraMonitoringInsightsUnsubscribeResponse(SdkBaseModel):
    """CraMonitoringInsightsUnsubscribeResponse defines the response schema for
    ``/cra/monitoring_insights/unsubscribe``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CraMonitoringInsightsUnsubscribeResponseDict(TypedDict):
    request_id: str
