from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .business_digital_presence_check import BusinessDigitalPresenceCheck, BusinessDigitalPresenceCheckDict
from .business_kybcheck import BusinessKybcheck, BusinessKybcheckDict
from .business_risk_check import BusinessRiskCheck, BusinessRiskCheckDict
from .business_search_terms import BusinessSearchTerms, BusinessSearchTermsDict
from .enums.business_verification_status_overall import BusinessVerificationStatusOverallOrStr


class BusinessVerificationGetResponse(SdkBaseModel):
    """A business verification represents a check of a business's identity and risk profile, including information
    collected about the business and results from third-party data providers."""

    id: str
    """ID of the associated business verification."""

    client_user_id: str
    """A unique ID that identifies the end user in your system. Either a ``user_id`` or the ``client_user_id`` must be
    provided. This ID can also be used to associate user-specific data from other Plaid products. Financial Account
    Matching requires this field and the ``/link/token/create`` ``client_user_id`` to be consistent. Personally
    identifiable information, such as an email address or phone number, should not be used in the ``client_user_id``."""

    created_at: RFC3339DateTime
    """An ISO8601 formatted timestamp."""

    completed_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    redacted_at: RFC3339DateTime | None
    """An ISO8601 formatted timestamp."""

    status: BusinessVerificationStatusOverallOrStr
    """Status of the overall business verification"""

    search_terms: BusinessSearchTerms
    """The business information that was used to perform the verification search"""

    kyb_check: BusinessKybcheck | None
    """Results from the KYB (Know Your Business) identity verification check"""

    risk_check: BusinessRiskCheck | None
    """Results from the business risk assessment check"""

    digital_presence_check: BusinessDigitalPresenceCheck | None
    """Results from the digital presence check."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    shareable_url: str | None
    """A shareable URL that can be sent directly to the user to complete verification"""


class BusinessVerificationGetResponseDict(TypedDict):
    id: str
    client_user_id: str
    created_at: RFC3339DateTime
    completed_at: RFC3339DateTime | None
    redacted_at: RFC3339DateTime | None
    status: BusinessVerificationStatusOverallOrStr
    search_terms: BusinessSearchTerms | BusinessSearchTermsDict
    kyb_check: BusinessKybcheck | BusinessKybcheckDict | None
    risk_check: BusinessRiskCheck | BusinessRiskCheckDict | None
    digital_presence_check: BusinessDigitalPresenceCheck | BusinessDigitalPresenceCheckDict | None
    request_id: str
    shareable_url: str | None
