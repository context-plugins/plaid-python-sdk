from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.income_verification_source_type import IncomeVerificationSourceTypeOrStr
from .sandbox_public_token_create_request_income_verification_bank_income import (
    SandboxPublicTokenCreateRequestIncomeVerificationBankIncome,
    SandboxPublicTokenCreateRequestIncomeVerificationBankIncomeDict,
)


class SandboxPublicTokenCreateRequestOptionsIncomeVerification(SdkBaseModel):
    """A set of parameters for income verification options. This field is required if ``income_verification`` is
    included in the ``initial_products`` array."""

    income_source_types: Optional[list[IncomeVerificationSourceTypeOrStr]] = UNSET
    """The types of source income data that users will be permitted to share. Options include ``bank`` and ``payroll``.
    Currently you can only specify one of these options."""

    bank_income: Optional[SandboxPublicTokenCreateRequestIncomeVerificationBankIncome] = UNSET
    """Specifies options for Bank Income. This field is required if ``income_verification`` is included in the
    ``initial_products`` array and ``bank`` is specified in ``income_source_types``."""


class SandboxPublicTokenCreateRequestOptionsIncomeVerificationDict(TypedDict):
    income_source_types: NotRequired[list[IncomeVerificationSourceTypeOrStr]]
    bank_income: NotRequired[
        (
            SandboxPublicTokenCreateRequestIncomeVerificationBankIncome
            | SandboxPublicTokenCreateRequestIncomeVerificationBankIncomeDict
        )
    ]
