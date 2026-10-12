from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .business_field_match_summary import BusinessFieldMatchSummary, BusinessFieldMatchSummaryDict
from .business_kybmatch_details import BusinessKybmatchDetails, BusinessKybmatchDetailsDict
from .enums.business_verification_status import BusinessVerificationStatusOrStr


class BusinessKybcheck(SdkBaseModel):
    """Results from the KYB (Know Your Business) identity verification check"""

    status: BusinessVerificationStatusOrStr
    """Status of the KYB (Know Your Business) identity assessment check"""

    score: int
    """A score from 0 to 100 indicating the confidence in KYB (Know Your Business) identity assessment for the
    business"""

    name: BusinessFieldMatchSummary
    """Summary of how a specific business field matched against data provider results"""

    address: BusinessFieldMatchSummary
    """Summary of how a specific business field matched against data provider results"""

    website: BusinessFieldMatchSummary
    """Summary of how a specific business field matched against data provider results"""

    match_details: BusinessKybmatchDetails | None
    """Detailed information about the business from data provider results"""


class BusinessKybcheckDict(TypedDict):
    status: BusinessVerificationStatusOrStr
    score: int
    name: BusinessFieldMatchSummaryDict
    address: BusinessFieldMatchSummaryDict
    website: BusinessFieldMatchSummaryDict
    match_details: BusinessKybmatchDetailsDict | None
