from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_match_summary_analysis import BeaconMatchSummaryAnalysis, BeaconMatchSummaryAnalysisDict
from .beacon_user_revision import BeaconUserRevision, BeaconUserRevisionDict


class BeaconDuplicateGetResponse(SdkBaseModel):
    """A Beacon Duplicate represents a pair of matching Beacon Users and an analysis of the fields they matched on."""

    id: str
    """ID of the associated Beacon Duplicate."""

    beacon_user1: BeaconUserRevision
    """A Beacon User Revision identifies a Beacon User at some point in its revision history."""

    beacon_user2: BeaconUserRevision
    """A Beacon User Revision identifies a Beacon User at some point in its revision history."""

    analysis: BeaconMatchSummaryAnalysis
    """Analysis of which fields matched between one Beacon User and another."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class BeaconDuplicateGetResponseDict(TypedDict):
    id: str
    beacon_user1: BeaconUserRevisionDict
    beacon_user2: BeaconUserRevisionDict
    analysis: BeaconMatchSummaryAnalysisDict
    request_id: str
