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


class CreditPayrollIncomePrecheckRequest(SdkBaseModel):
    """Defines the request schema for ``/credit/payroll_income/precheck``."""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    user_token: Optional[str] = UNSET
    """The user token associated with the user for which data is being requested. This field is used only by customers
    with pre-existing integrations that already use the ``user_token`` field. All other customers should use the
    ``user_id`` instead. For more details, see `New User APIs <https://plaid.com/docs/api/users/user-apis>`__."""

    user_id: Optional[str] = UNSET
    access_tokens: Optional[list[str]] = UNSET
    """An array of access tokens corresponding to Items belonging to the user whose eligibility is being checked. Note
    that if the Items specified here are not already initialized with ``transactions``, providing them in this field
    will cause these Items to be initialized with (and billed for) the Transactions product."""

    employer: OptionalNullable[IncomeVerificationPrecheckEmployer] = UNSET
    """Information about the end user's employer"""

    us_military_info: OptionalNullable[IncomeVerificationPrecheckMilitaryInfo] = UNSET
    """Data about military info in the income verification precheck."""

    payroll_institution: OptionalNullable[IncomeVerificationPrecheckPayrollInstitution] = UNSET
    """Information about the end user's payroll institution"""


class CreditPayrollIncomePrecheckRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_token: NotRequired[str]
    user_id: NotRequired[str]
    access_tokens: NotRequired[list[str]]
    employer: NotRequired[IncomeVerificationPrecheckEmployerDict | None]
    us_military_info: NotRequired[IncomeVerificationPrecheckMilitaryInfoDict | None]
    payroll_institution: NotRequired[IncomeVerificationPrecheckPayrollInstitutionDict | None]
