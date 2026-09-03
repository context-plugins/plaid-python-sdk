from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_report_syndication_analysis import BeaconReportSyndicationAnalysis, BeaconReportSyndicationAnalysisDict
from .beacon_report_syndication_original_report import (
    BeaconReportSyndicationOriginalReport,
    BeaconReportSyndicationOriginalReportDict,
)


class BeaconReportSyndication(SdkBaseModel):
    """A Beacon Report Syndication represents a Beacon Report created either by your organization or another Beacon
    customer that matches a specific Beacon User you've created.

    The ``analysis`` field in the response indicates which fields matched between the originally reported Beacon User
    and the Beacon User that the report was syndicated to.

    The ``report`` field in the response contains a subset of information from the original report."""

    id: str
    """ID of the associated Beacon Report Syndication."""

    beacon_user_id: str
    """ID of the associated Beacon User."""

    report: BeaconReportSyndicationOriginalReport
    """A subset of information from a Beacon Report that has been syndicated to a matching Beacon User in your program.

    The ``id`` field in the response is the ID of the original report that was syndicated. If the original report was
    created by your organization, the field will be filled with the ID of the report. Otherwise, the field will be
    ``null`` indicating that the original report was created by another Beacon customer."""

    analysis: BeaconReportSyndicationAnalysis
    """Analysis of which fields matched between the originally reported Beacon User and the Beacon User that the report
    was syndicated to."""


class BeaconReportSyndicationDict(TypedDict):
    id: str
    beacon_user_id: str
    report: BeaconReportSyndicationOriginalReport | BeaconReportSyndicationOriginalReportDict
    analysis: BeaconReportSyndicationAnalysis | BeaconReportSyndicationAnalysisDict
