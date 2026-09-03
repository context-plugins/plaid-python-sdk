from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.match_summary_code import MatchSummaryCodeOrStr


class KyccheckIdnumberSummary(SdkBaseModel):
    """Result summary object specifying how the ``id_number`` field matched."""

    summary: MatchSummaryCodeOrStr
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""


class KyccheckIdnumberSummaryDict(TypedDict):
    summary: MatchSummaryCodeOrStr
