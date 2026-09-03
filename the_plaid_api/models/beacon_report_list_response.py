from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_report import BeaconReport, BeaconReportDict


class BeaconReportListResponse(SdkBaseModel):
    """The response schema for ``/beacon/report/list``"""

    beacon_reports: list[BeaconReport]
    next_cursor: str | None
    """An identifier that determines which page of results you receive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BeaconReportListResponseDict(TypedDict):
    beacon_reports: list[BeaconReport | BeaconReportDict]
    next_cursor: str | None
    request_id: str
