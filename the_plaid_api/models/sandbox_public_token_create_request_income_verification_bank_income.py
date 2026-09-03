from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SandboxPublicTokenCreateRequestIncomeVerificationBankIncome(SdkBaseModel):
    """Specifies options for Bank Income. This field is required if ``income_verification`` is included in the
    ``initial_products`` array and ``bank`` is specified in ``income_source_types``."""

    days_requested: Optional[int] = UNSET
    """The number of days of data to request for the Bank Income product"""


class SandboxPublicTokenCreateRequestIncomeVerificationBankIncomeDict(TypedDict):
    days_requested: NotRequired[int]
