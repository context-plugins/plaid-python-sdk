from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProtectReportCreateResponse(SdkBaseModel):
    """Response object for /protect/report/create"""

    report_id: str
    """A unique identifier representing the submitted report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProtectReportCreateResponseDict(TypedDict):
    report_id: str
    request_id: str
