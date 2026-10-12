from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_filter import CreditFilter, CreditFilterDict
from .depository_filter import DepositoryFilter, DepositoryFilterDict
from .investment_filter import InvestmentFilter, InvestmentFilterDict
from .loan_filter import LoanFilter, LoanFilterDict


class AccountFiltersResponse(SdkBaseModel):
    """The ``account_filters`` specified in the original call to ``/link/token/create``."""

    depository: Optional[DepositoryFilter] = UNSET
    """A filter to apply to ``depository``-type accounts"""

    credit: Optional[CreditFilter] = UNSET
    """A filter to apply to ``credit``-type accounts"""

    loan: Optional[LoanFilter] = UNSET
    """A filter to apply to ``loan``-type accounts"""

    investment: Optional[InvestmentFilter] = UNSET
    """A filter to apply to ``investment``-type accounts (or ``brokerage``-type accounts for API versions 2018-05-22 and
    earlier)."""


class AccountFiltersResponseDict(TypedDict):
    depository: NotRequired[DepositoryFilterDict]
    credit: NotRequired[CreditFilterDict]
    loan: NotRequired[LoanFilterDict]
    investment: NotRequired[InvestmentFilterDict]
