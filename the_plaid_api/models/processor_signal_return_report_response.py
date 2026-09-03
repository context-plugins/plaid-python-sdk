from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProcessorSignalReturnReportResponse(SdkBaseModel):
    """ProcessorSignalReturnReportResponse defines the response schema for ``/processor/signal/return/report``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorSignalReturnReportResponseDict(TypedDict):
    request_id: str
