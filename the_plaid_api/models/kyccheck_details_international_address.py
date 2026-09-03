from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.hidden_match_summary_code import HiddenMatchSummaryCodeOrStr


class KyccheckDetailsInternationalAddress(SdkBaseModel):
    """Result summary object specifying how the ``address`` field matched for fields that are only present on an
    international KYC check."""

    building: HiddenMatchSummaryCodeOrStr
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    county: HiddenMatchSummaryCodeOrStr
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    district: HiddenMatchSummaryCodeOrStr
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    house_number: HiddenMatchSummaryCodeOrStr
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    subpremise: HiddenMatchSummaryCodeOrStr
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    thoroughfare: HiddenMatchSummaryCodeOrStr
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""


class KyccheckDetailsInternationalAddressDict(TypedDict):
    building: HiddenMatchSummaryCodeOrStr
    county: HiddenMatchSummaryCodeOrStr
    district: HiddenMatchSummaryCodeOrStr
    house_number: HiddenMatchSummaryCodeOrStr
    subpremise: HiddenMatchSummaryCodeOrStr
    thoroughfare: HiddenMatchSummaryCodeOrStr
