from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .business_field_match_summary import BusinessFieldMatchSummary, BusinessFieldMatchSummaryDict
from .business_website_analysis import BusinessWebsiteAnalysis, BusinessWebsiteAnalysisDict
from .enums.business_verification_status_web_presence_check import BusinessVerificationStatusWebPresenceCheckOrStr


class BusinessDigitalPresenceCheck(SdkBaseModel):
    """Results from the digital presence check."""

    status: BusinessVerificationStatusWebPresenceCheckOrStr
    """Status of the digital presence check"""

    score: int
    """A score from 0 to 100 indicating digital presence confidence."""

    address: BusinessFieldMatchSummary
    """Summary of how a specific business field matched against data provider results"""

    phone_number: BusinessFieldMatchSummary
    """Summary of how a specific business field matched against data provider results"""

    email_address: BusinessFieldMatchSummary
    """Summary of how a specific business field matched against data provider results"""

    website: BusinessFieldMatchSummary
    """Summary of how a specific business field matched against data provider results"""

    website_analysis: BusinessWebsiteAnalysis | None
    """Website analysis details if a website is found for the provided website in the search terms."""


class BusinessDigitalPresenceCheckDict(TypedDict):
    status: BusinessVerificationStatusWebPresenceCheckOrStr
    score: int
    address: BusinessFieldMatchSummaryDict
    phone_number: BusinessFieldMatchSummaryDict
    email_address: BusinessFieldMatchSummaryDict
    website: BusinessFieldMatchSummaryDict
    website_analysis: BusinessWebsiteAnalysisDict | None
