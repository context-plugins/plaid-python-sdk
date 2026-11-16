from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.partner_end_customer_cra_use_case import PartnerEndCustomerCraUseCaseOrStr


class PartnerEndCustomerCraUseCases(SdkBaseModel):
    """The list of use cases associated with a given permissible purpose."""

    use_cases: Optional[list[PartnerEndCustomerCraUseCaseOrStr]] = UNSET
    """List of use cases for the given permissible purpose."""


class PartnerEndCustomerCraUseCasesDict(TypedDict):
    use_cases: NotRequired[list[PartnerEndCustomerCraUseCaseOrStr]]
