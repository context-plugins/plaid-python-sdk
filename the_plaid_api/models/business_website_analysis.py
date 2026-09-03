from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .business_website_ssl import BusinessWebsiteSsl, BusinessWebsiteSslDict
from .business_whois_record import BusinessWhoisRecord, BusinessWhoisRecordDict
from .enums.business_check_boolean_status import BusinessCheckBooleanStatusOrStr
from .enums.business_website_build_status import BusinessWebsiteBuildStatusOrStr


class BusinessWebsiteAnalysis(SdkBaseModel):
    """Website analysis details if a website is found for the provided website in the search terms."""

    is_parked: BusinessCheckBooleanStatusOrStr
    """Tri-state boolean status, where ``no_data`` indicates the check could not determine a value."""

    email_is_deliverable: BusinessCheckBooleanStatusOrStr
    """Tri-state boolean status, where ``no_data`` indicates the check could not determine a value."""

    website_build_status: BusinessWebsiteBuildStatusOrStr
    """Build status of the business website."""

    whois_record: BusinessWhoisRecord
    """WHOIS metadata for the business website domain."""

    ssl: BusinessWebsiteSsl
    """SSL status for the business website."""


class BusinessWebsiteAnalysisDict(TypedDict):
    is_parked: BusinessCheckBooleanStatusOrStr
    email_is_deliverable: BusinessCheckBooleanStatusOrStr
    website_build_status: BusinessWebsiteBuildStatusOrStr
    whois_record: BusinessWhoisRecord | BusinessWhoisRecordDict
    ssl: BusinessWebsiteSsl | BusinessWebsiteSslDict
