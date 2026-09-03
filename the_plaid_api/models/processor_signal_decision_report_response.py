from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProcessorSignalDecisionReportResponse(SdkBaseModel):
    """ProcessorSignalDecisionReportResponse defines the response schema for ``/processor/signal/decision/report``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorSignalDecisionReportResponseDict(TypedDict):
    request_id: str
