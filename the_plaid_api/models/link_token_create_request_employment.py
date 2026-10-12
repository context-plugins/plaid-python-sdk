from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.employment_source_type import EmploymentSourceTypeOrStr
from .link_token_create_request_employment_bank_income import (
    LinkTokenCreateRequestEmploymentBankIncome,
    LinkTokenCreateRequestEmploymentBankIncomeDict,
)


class LinkTokenCreateRequestEmployment(SdkBaseModel):
    """Specifies options for initializing Link for use with the Employment product. This field is required if
    ``employment`` is included in the ``products`` array."""

    employment_source_types: Optional[list[EmploymentSourceTypeOrStr]] = UNSET
    """The types of source employment data that users will be permitted to share. Options include ``bank`` and
    ``payroll``. Currently you can only specify one of these options."""

    bank_employment: Optional[LinkTokenCreateRequestEmploymentBankIncome] = UNSET
    """Specifies options for initializing Link for use with Bank Employment. This field is required if ``employment`` is
    included in the ``products`` array and ``bank`` is specified in ``employment_source_types``."""


class LinkTokenCreateRequestEmploymentDict(TypedDict):
    employment_source_types: NotRequired[list[EmploymentSourceTypeOrStr]]
    bank_employment: NotRequired[LinkTokenCreateRequestEmploymentBankIncomeDict]
