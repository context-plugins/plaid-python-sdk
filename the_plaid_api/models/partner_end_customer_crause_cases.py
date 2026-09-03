from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.partner_end_customer_crause_case import PartnerEndCustomerCrauseCaseOrStr


class PartnerEndCustomerCrauseCases(SdkBaseModel):
    """The list of use cases associated with a given permissible purpose."""

    use_cases: Optional[list[PartnerEndCustomerCrauseCaseOrStr]] = UNSET
    """List of use cases for the given permissible purpose."""


class PartnerEndCustomerCrauseCasesDict(TypedDict):
    use_cases: NotRequired[list[PartnerEndCustomerCrauseCaseOrStr]]
