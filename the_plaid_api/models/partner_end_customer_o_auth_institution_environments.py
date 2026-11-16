from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.partner_end_customer_o_auth_institution_application_status import (
    PartnerEndCustomerOAuthInstitutionApplicationStatusOrStr,
)


class PartnerEndCustomerOAuthInstitutionEnvironments(SdkBaseModel):
    """Registration statuses by environment."""

    development: Optional[PartnerEndCustomerOAuthInstitutionApplicationStatusOrStr] = UNSET
    """The registration status for the end customer's application."""

    production: Optional[PartnerEndCustomerOAuthInstitutionApplicationStatusOrStr] = UNSET
    """The registration status for the end customer's application."""


class PartnerEndCustomerOAuthInstitutionEnvironmentsDict(TypedDict):
    development: NotRequired[PartnerEndCustomerOAuthInstitutionApplicationStatusOrStr]
    production: NotRequired[PartnerEndCustomerOAuthInstitutionApplicationStatusOrStr]
