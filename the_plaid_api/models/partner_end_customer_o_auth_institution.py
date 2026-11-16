from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .error import Error, ErrorDict
from .partner_end_customer_o_auth_institution_environments import (
    PartnerEndCustomerOAuthInstitutionEnvironments,
    PartnerEndCustomerOAuthInstitutionEnvironmentsDict,
)


class PartnerEndCustomerOAuthInstitution(SdkBaseModel):
    """The OAuth registration information for an institution."""

    name: Optional[str] = UNSET
    institution_id: Optional[str] = UNSET
    environments: Optional[PartnerEndCustomerOAuthInstitutionEnvironments] = UNSET
    """Registration statuses by environment."""

    production_enablement_date: OptionalNullable[str] = UNSET
    """The date on which the end customer's application was approved by the institution, or an empty string if their
    application has not yet been approved."""

    classic_disablement_date: OptionalNullable[str] = UNSET
    """The date on which non-OAuth Item adds will no longer be supported for this institution, or an empty string if no
    such date has been set by the institution."""

    errors: Optional[list[Error | None]] = UNSET
    """The errors encountered while registering the end customer's application with the institutions."""


class PartnerEndCustomerOAuthInstitutionDict(TypedDict):
    name: NotRequired[str]
    institution_id: NotRequired[str]
    environments: NotRequired[PartnerEndCustomerOAuthInstitutionEnvironmentsDict]
    production_enablement_date: NotRequired[str | None]
    classic_disablement_date: NotRequired[str | None]
    errors: NotRequired[list[ErrorDict | None]]
