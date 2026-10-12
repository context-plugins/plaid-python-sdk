from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_syndicated_report_depository_account_match_analysis import (
    BeaconSyndicatedReportDepositoryAccountMatchAnalysis,
    BeaconSyndicatedReportDepositoryAccountMatchAnalysisDict,
)
from .enums.beacon_match_summary_code import BeaconMatchSummaryCodeOrStr


class BeaconReportSyndicationAnalysis(SdkBaseModel):
    """Analysis of which fields matched between the originally reported Beacon User and the Beacon User that the report
    was syndicated to."""

    address: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""

    date_of_birth: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""

    email_address: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""

    name: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""

    id_number: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""

    ip_address: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""

    phone_number: BeaconMatchSummaryCodeOrStr
    """An enum indicating the match type between two Beacon Users.


    ``match`` indicates that the provided input data was a strong match against the other Beacon User.

    ``partial_match`` indicates the data approximately matched the other Beacon User. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to compare this field against the other Beacon User and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to compare this field against the original Beacon User because the field
    was not present in one of the Beacon Users."""

    depository_accounts: list[BeaconSyndicatedReportDepositoryAccountMatchAnalysis]


class BeaconReportSyndicationAnalysisDict(TypedDict):
    address: BeaconMatchSummaryCodeOrStr
    date_of_birth: BeaconMatchSummaryCodeOrStr
    email_address: BeaconMatchSummaryCodeOrStr
    name: BeaconMatchSummaryCodeOrStr
    id_number: BeaconMatchSummaryCodeOrStr
    ip_address: BeaconMatchSummaryCodeOrStr
    phone_number: BeaconMatchSummaryCodeOrStr
    depository_accounts: list[BeaconSyndicatedReportDepositoryAccountMatchAnalysisDict]
