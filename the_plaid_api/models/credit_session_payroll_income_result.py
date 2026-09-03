from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreditSessionPayrollIncomeResult(SdkBaseModel):
    """The details of a digital payroll income verification in Link"""

    num_paystubs_retrieved: Optional[int] = UNSET
    """The number of paystubs retrieved from a payroll provider."""

    num_w2s_retrieved: Optional[int] = UNSET
    """The number of w2s retrieved from a payroll provider."""

    institution_id: Optional[str] = UNSET
    """The Plaid Institution ID associated with the Item."""

    institution_name: Optional[str] = UNSET
    """The Institution Name associated with the Item."""


class CreditSessionPayrollIncomeResultDict(TypedDict):
    num_paystubs_retrieved: NotRequired[int]
    num_w2s_retrieved: NotRequired[int]
    institution_id: NotRequired[str]
    institution_name: NotRequired[str]
