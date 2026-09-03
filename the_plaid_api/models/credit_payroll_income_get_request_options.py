from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditPayrollIncomeGetRequestOptions(SdkBaseModel):
    """An optional object for ``/credit/payroll_income/get`` request options."""

    item_ids: Optional[list[str]] = UNSET
    """An array of ``item_id``s whose payroll information is returned. Each ``item_id`` should uniquely identify a
    payroll income item. If this field is not provided, all ``item_id``s associated with the ``user_token`` will be
    returned in the response."""


class CreditPayrollIncomeGetRequestOptionsDict(TypedDict):
    item_ids: NotRequired[list[str]]
