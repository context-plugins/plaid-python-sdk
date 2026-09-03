from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.match_summary_code import MatchSummaryCodeOrStr


class ScreeningHitAnalysis(SdkBaseModel):
    """Analysis information describing why a screening hit matched the provided user information"""

    dates_of_birth: Optional[MatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

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

    search_terms_version: int
    """The version of the screening's ``search_terms`` that were compared when the screening hit was added. Screening
    hits are immutable once they have been reviewed. If changes are detected due to updates to the screening's
    ``search_terms``, the associated program, or the list's source data prior to review, the screening hit will be
    updated to reflect those changes."""


class ScreeningHitAnalysisDict(TypedDict):
    dates_of_birth: NotRequired[MatchSummaryCodeOrStr]
    documents: NotRequired[MatchSummaryCodeOrStr]
    locations: NotRequired[MatchSummaryCodeOrStr]
    names: NotRequired[MatchSummaryCodeOrStr]
    search_terms_version: int
