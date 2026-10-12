from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.address_purpose_label import AddressPurposeLabelOrStr
from .enums.hidden_match_summary_code import HiddenMatchSummaryCodeOrStr
from .enums.match_summary_code import MatchSummaryCodeOrStr
from .enums.pobox_status import PoboxStatusOrStr
from .kyccheck_details_international_address import (
    KyccheckDetailsInternationalAddress,
    KyccheckDetailsInternationalAddressDict,
)


class KyccheckAddressSummary(SdkBaseModel):
    """Result summary object specifying how the ``address`` field matched."""

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

    po_box: PoboxStatusOrStr
    """Field describing whether the associated address is a post office box. Will be ``yes`` when a P.O. box is
    detected, ``no`` when Plaid confirmed the address is not a P.O. box, and ``no_data`` when Plaid was not able to
    determine if the address is a P.O. box."""

    type_: AddressPurposeLabelOrStr = Field(alias="type")
    """Field describing whether the associated address is being used for commercial or residential purposes.

    Note: This value will be ``no_data`` when Plaid does not have sufficient data to determine the address's use."""

    street: Optional[HiddenMatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    city: Optional[HiddenMatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    region: Optional[HiddenMatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    postal_code: Optional[HiddenMatchSummaryCodeOrStr] = UNSET
    """An enum indicating the match type between data provided by user and data checked against an external data source.


    ``match`` indicates that the provided input data was a strong match against external data.

    ``partial_match`` indicates the data approximately matched against external data. For example, "Knope" vs.
    "Knope-Wyatt" for last name.

    ``no_match`` indicates that Plaid was able to perform a check against an external data source and it did not match
    the provided input data.

    ``no_data`` indicates that Plaid was unable to find external data to compare against the provided input data.

    ``no_input`` indicates that Plaid was unable to perform a check because no information was provided for this field
    by the end user."""

    international_details: OptionalNullable[KyccheckDetailsInternationalAddress] = UNSET
    """Result summary object specifying how the ``address`` field matched for fields that are only present on an
    international KYC check."""


class KyccheckAddressSummaryDict(TypedDict):
    summary: MatchSummaryCodeOrStr
    po_box: PoboxStatusOrStr
    type_: AddressPurposeLabelOrStr
    street: NotRequired[HiddenMatchSummaryCodeOrStr]
    city: NotRequired[HiddenMatchSummaryCodeOrStr]
    region: NotRequired[HiddenMatchSummaryCodeOrStr]
    postal_code: NotRequired[HiddenMatchSummaryCodeOrStr]
    international_details: NotRequired[KyccheckDetailsInternationalAddressDict | None]
