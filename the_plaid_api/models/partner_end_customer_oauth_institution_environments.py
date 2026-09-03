from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.partner_end_customer_oauth_institution_application_status import (
    PartnerEndCustomerOauthInstitutionApplicationStatusOrStr,
)


class PartnerEndCustomerOauthInstitutionEnvironments(SdkBaseModel):
    """Registration statuses by environment."""

    development: Optional[PartnerEndCustomerOauthInstitutionApplicationStatusOrStr] = UNSET
    """The registration status for the end customer's application."""

    production: Optional[PartnerEndCustomerOauthInstitutionApplicationStatusOrStr] = UNSET
    """The registration status for the end customer's application."""


class PartnerEndCustomerOauthInstitutionEnvironmentsDict(TypedDict):
    development: NotRequired[PartnerEndCustomerOauthInstitutionApplicationStatusOrStr]
    production: NotRequired[PartnerEndCustomerOauthInstitutionApplicationStatusOrStr]
