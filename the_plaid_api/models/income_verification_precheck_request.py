from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .income_verification_precheck_employer import (
    IncomeVerificationPrecheckEmployer,
    IncomeVerificationPrecheckEmployerDict,
)
from .income_verification_precheck_military_info import (
    IncomeVerificationPrecheckMilitaryInfo,
    IncomeVerificationPrecheckMilitaryInfoDict,
)
from .income_verification_precheck_payroll_institution import (
    IncomeVerificationPrecheckPayrollInstitution,
    IncomeVerificationPrecheckPayrollInstitutionDict,
)
from .income_verification_precheck_user import IncomeVerificationPrecheckUser, IncomeVerificationPrecheckUserDict


class IncomeVerificationPrecheckRequest(SdkBaseModel):
    """IncomeVerificationPrecheckRequest defines the request schema for ``/income/verification/precheck``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user: OptionalNullable[IncomeVerificationPrecheckUser] = UNSET
    """Information about the user whose eligibility is being evaluated."""

    employer: OptionalNullable[IncomeVerificationPrecheckEmployer] = UNSET
    """Information about the end user's employer"""

    payroll_institution: OptionalNullable[IncomeVerificationPrecheckPayrollInstitution] = UNSET
    """Information about the end user's payroll institution"""

    transactions_access_token: OptionalNullable[str] = UNSET
    transactions_access_tokens: Optional[list[str]] = UNSET
    """An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note
    that if the Items specified here are not already initialized with ``transactions``, providing them in this field
    will cause these Items to be initialized with (and billed for) the Transactions product."""

    us_military_info: OptionalNullable[IncomeVerificationPrecheckMilitaryInfo] = UNSET
    """Data about military info in the income verification precheck."""


class IncomeVerificationPrecheckRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user: NotRequired[IncomeVerificationPrecheckUser | IncomeVerificationPrecheckUserDict | None]
    employer: NotRequired[IncomeVerificationPrecheckEmployer | IncomeVerificationPrecheckEmployerDict | None]
    payroll_institution: NotRequired[
        IncomeVerificationPrecheckPayrollInstitution | IncomeVerificationPrecheckPayrollInstitutionDict | None
    ]
    transactions_access_token: NotRequired[str | None]
    transactions_access_tokens: NotRequired[list[str]]
    us_military_info: NotRequired[
        IncomeVerificationPrecheckMilitaryInfo | IncomeVerificationPrecheckMilitaryInfoDict | None
    ]
