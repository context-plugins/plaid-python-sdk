from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.match_summary_code import MatchSummaryCodeOrStr


class EntityScreeningHitAnalysis(SdkBaseModel):
    """Analysis information describing why a screening hit matched the provided entity information"""

    documents: Optional[MatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    email_addresses: Optional[MatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    locations: Optional[MatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    names: Optional[MatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    phone_numbers: Optional[MatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    urls: Optional[MatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    search_terms_version: int
    """The version of the entity screening's ``search_terms`` that were compared when the entity screening hit was
    added. Entity screening hits are immutable once they have been reviewed. If changes are detected due to updates to
    the entity screening's ``search_terms``, the associated entity program, or the list's source data prior to review,
    the entity screening hit will be updated to reflect those changes."""


class EntityScreeningHitAnalysisDict(TypedDict):
    documents: NotRequired[MatchSummaryCodeOrStr]
    email_addresses: NotRequired[MatchSummaryCodeOrStr]
    locations: NotRequired[MatchSummaryCodeOrStr]
    names: NotRequired[MatchSummaryCodeOrStr]
    phone_numbers: NotRequired[MatchSummaryCodeOrStr]
    urls: NotRequired[MatchSummaryCodeOrStr]
    search_terms_version: int
