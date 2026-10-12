from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .cra_credit_profile_lend_score import CraCreditProfileLendScore, CraCreditProfileLendScoreDict
from .cra_credit_profile_report_metadata import CraCreditProfileReportMetadata, CraCreditProfileReportMetadataDict
from .enums.cra_credit_profile_inquiry_type import CraCreditProfileInquiryTypeOrStr


class CraCreditProfileReport(SdkBaseModel):
    """Contains data for the CRA Credit Profile Report."""

    date_retrieved: RFC3339DateTime
    """The time when the report was retrieved."""

    inquiry_type: CraCreditProfileInquiryTypeOrStr
    """The inquiry type of credit profile report."""

    client_report_id: str
    """Client-generated identifier, which can be used by lenders to track loan applications."""

    lend_scores: list[CraCreditProfileLendScore | None]
    """The LendScore results for the credit profile report."""

    cashflow_insights_attributes: dict[str, Any] | None
    """A map of cash flow attributes, where the key is a string, and the value is a string, float, int, or boolean. The
    specific list of attributes will depend on the cash flow attributes version used. For a full list of attributes,
    contact your account manager."""

    network_insights_attributes: dict[str, Any] | None
    """A map of network attributes, where the key is a string, and the value is a float, int, or boolean. For a full
    list of attributes, contact your account manager."""

    metadata: CraCreditProfileReportMetadata | None
    """Metadata about the CRA Credit Profile Report."""


class CraCreditProfileReportDict(TypedDict):
    date_retrieved: RFC3339DateTime
    inquiry_type: CraCreditProfileInquiryTypeOrStr
    client_report_id: str
    lend_scores: list[CraCreditProfileLendScoreDict | None]
    cashflow_insights_attributes: dict[str, Any] | None
    network_insights_attributes: dict[str, Any] | None
    metadata: CraCreditProfileReportMetadataDict | None
