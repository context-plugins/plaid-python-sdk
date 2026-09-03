from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditPayrollIncomeRefreshRequestOptions(SdkBaseModel):
    """An optional object for ``/credit/payroll_income/refresh`` request options."""

    item_ids: Optional[list[str]] = UNSET
    """An array of ``item_id``s to be refreshed. Each ``item_id`` should uniquely identify a payroll income item. If
    this field is not provided, all ``item_id``s associated with the ``user_token`` will be refreshed."""

    webhook: Optional[str] = UNSET
    """The URL where Plaid will send the payroll income refresh webhook."""


class CreditPayrollIncomeRefreshRequestOptionsDict(TypedDict):
    item_ids: NotRequired[list[str]]
    webhook: NotRequired[str]
