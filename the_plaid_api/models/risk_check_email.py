from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.risk_check_email_domain_is_custom import RiskCheckEmailDomainIsCustomOrStr
from .enums.risk_check_email_domain_is_disposable import RiskCheckEmailDomainIsDisposableOrStr
from .enums.risk_check_email_domain_is_free_provider import RiskCheckEmailDomainIsFreeProviderOrStr
from .enums.risk_check_email_includes_date_of_birth import RiskCheckEmailIncludesDateOfBirthOrStr
from .enums.risk_check_email_is_deliverable_status import RiskCheckEmailIsDeliverableStatusOrStr
from .enums.risk_check_email_is_edu import RiskCheckEmailIsEduOrStr
from .enums.risk_check_email_name import RiskCheckEmailNameOrStr
from .enums.risk_check_email_top_level_domain_is_suspicious import RiskCheckEmailTopLevelDomainIsSuspiciousOrStr
from .enums.risk_check_linked_service import RiskCheckLinkedServiceOrStr
from .enums.risk_level import RiskLevelOrStr


class RiskCheckEmail(SdkBaseModel):
    """Result summary object specifying values for ``email`` attributes of risk check."""

    is_deliverable: RiskCheckEmailIsDeliverableStatusOrStr
    """SMTP-MX check to confirm the email address exists if known."""

    breach_count: int | None
    """Count of all known breaches of this email address if known."""

    first_breached_at: Date | None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    last_breached_at: Date | None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    domain_registered_at: Date | None
    """A date in the format YYYY-MM-DD (RFC 3339 Section 5.6)."""

    domain_is_free_provider: RiskCheckEmailDomainIsFreeProviderOrStr
    """Indicates whether the email address domain is a free provider such as Gmail or Hotmail if known."""

    domain_is_custom: RiskCheckEmailDomainIsCustomOrStr
    """Indicates whether the email address domain is custom if known, i.e. a company domain and not free or
    disposable."""

    domain_is_disposable: RiskCheckEmailDomainIsDisposableOrStr
    """Indicates whether the email domain is listed as disposable if known. Disposable domains are often used to create
    email addresses that are part of a fake set of user details."""

    top_level_domain_is_suspicious: RiskCheckEmailTopLevelDomainIsSuspiciousOrStr
    """Indicates whether the email address top level domain, which is the last part of the domain, is fraudulent or
    risky if known. In most cases, a suspicious top level domain is also associated with a disposable or high-risk
    domain."""

    is_edu: RiskCheckEmailIsEduOrStr
    """Indicates whether the email address domain is an educational institution domain if known."""

    includes_date_of_birth: RiskCheckEmailIncludesDateOfBirthOrStr
    """Indicates whether the email address includes the date of birth or year of birth if known."""

    name: RiskCheckEmailNameOrStr
    """Indicates whether the provided name matches the email address according to the KYC name-matches-email inference
    result if known.

    ``match`` - "The email's name identifiers match the user's name."

    ``partial_match`` - "The email's name identifiers partially match the user's name."

    ``no_match`` - "The email's name identifiers do not match the user's name."

    ``indeterminate`` - "The email does not contain any name identifiers, and a match could not be determined."

    ``no_input`` - "The user's profile does not contain the required user inputs to determine a match."

    ``no_data`` - "Field could not be verified against available sources."
    """

    linked_services: list[RiskCheckLinkedServiceOrStr]
    """A list of online services where this email address has been detected to have accounts or other activity."""

    risk_level: Optional[RiskLevelOrStr] = UNSET
    """Risk level for the given risk check type."""

    factors: Optional[list[str]] = UNSET
    """List of factors, when available, that contribute towards the risk level of the given risk check type."""


class RiskCheckEmailDict(TypedDict):
    is_deliverable: RiskCheckEmailIsDeliverableStatusOrStr
    breach_count: int | None
    first_breached_at: Date | None
    last_breached_at: Date | None
    domain_registered_at: Date | None
    domain_is_free_provider: RiskCheckEmailDomainIsFreeProviderOrStr
    domain_is_custom: RiskCheckEmailDomainIsCustomOrStr
    domain_is_disposable: RiskCheckEmailDomainIsDisposableOrStr
    top_level_domain_is_suspicious: RiskCheckEmailTopLevelDomainIsSuspiciousOrStr
    is_edu: RiskCheckEmailIsEduOrStr
    includes_date_of_birth: RiskCheckEmailIncludesDateOfBirthOrStr
    name: RiskCheckEmailNameOrStr
    linked_services: list[RiskCheckLinkedServiceOrStr]
    risk_level: NotRequired[RiskLevelOrStr]
    factors: NotRequired[list[str]]
