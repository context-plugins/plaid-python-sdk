from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_report_syndication import BeaconReportSyndication, BeaconReportSyndicationDict


class BeaconReportSyndicationListResponse(SdkBaseModel):
    """The response schema for ``/beacon/report_syndication/list``"""

    beacon_report_syndications: list[BeaconReportSyndication]
    next_cursor: str | None
    """An identifier that determines which page of results you receive."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BeaconReportSyndicationListResponseDict(TypedDict):
    beacon_report_syndications: list[BeaconReportSyndication | BeaconReportSyndicationDict]
    next_cursor: str | None
    request_id: str
