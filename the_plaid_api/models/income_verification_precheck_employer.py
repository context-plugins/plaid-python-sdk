from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .income_verification_precheck_employer_address import (
    IncomeVerificationPrecheckEmployerAddress,
    IncomeVerificationPrecheckEmployerAddressDict,
)


class IncomeVerificationPrecheckEmployer(SdkBaseModel):
    """Information about the end user's employer"""

    name: OptionalNullable[str] = UNSET
    """The employer's name"""

    address: OptionalNullable[IncomeVerificationPrecheckEmployerAddress] = UNSET
    """The address of the employer"""

    tax_id: OptionalNullable[str] = UNSET
    """The employer's tax id"""

    url: OptionalNullable[str] = UNSET
    """The URL for the employer's public website"""


class IncomeVerificationPrecheckEmployerDict(TypedDict):
    name: NotRequired[str | None]
    address: NotRequired[
        IncomeVerificationPrecheckEmployerAddress | IncomeVerificationPrecheckEmployerAddressDict | None
    ]
    tax_id: NotRequired[str | None]
    url: NotRequired[str | None]
