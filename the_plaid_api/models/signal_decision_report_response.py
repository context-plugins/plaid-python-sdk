from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SignalDecisionReportResponse(SdkBaseModel):
    """SignalDecisionReportResponse defines the response schema for ``/signal/decision/report``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SignalDecisionReportResponseDict(TypedDict):
    request_id: str
