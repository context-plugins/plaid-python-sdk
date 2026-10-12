from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_payroll_income_get_request_options import (
    CreditPayrollIncomeGetRequestOptions,
    CreditPayrollIncomeGetRequestOptionsDict,
)


class CreditPayrollIncomeGetRequest(SdkBaseModel):
    """CreditPayrollIncomeGetRequest defines the request schema for ``/credit/payroll_income/get``."""

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
    options: Optional[CreditPayrollIncomeGetRequestOptions] = UNSET
    """An optional object for ``/credit/payroll_income/get`` request options."""


class CreditPayrollIncomeGetRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    user_token: NotRequired[str]
    user_id: NotRequired[str]
    options: NotRequired[CreditPayrollIncomeGetRequestOptionsDict]
