from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.beacon_match_summary_code import BeaconMatchSummaryCodeOrStr


class BeaconSyndicatedReportDepositoryAccountMatchAnalysis(SdkBaseModel):
    """Analysis of whether this account matched between the originally reported Beacon User and the Beacon User that the
    report syndicated to."""

    account_mask: str
    """The last 2-4 numeric characters of this account's account number."""

    routing_number: str
    """The routing number of the account."""

    match_status: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""


class BeaconSyndicatedReportDepositoryAccountMatchAnalysisDict(TypedDict):
    account_mask: str
    routing_number: str
    match_status: BeaconMatchSummaryCodeOrStr
