from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CraMonitoringInsightsUnsubscribeRequest(SdkBaseModel):
    """CraMonitoringInsightsUnsubscribeRequest defines the request schema for
    ``/cra/monitoring_insights/unsubscribe``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    subscription_id: str
    """A unique identifier for the subscription."""


class CraMonitoringInsightsUnsubscribeRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    subscription_id: str
