from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.income_breakdown_type import IncomeBreakdownTypeOrStr


class IncomeBreakdown(SdkBaseModel):
    """An object representing a breakdown of the different income types on the paystub."""

    type_: IncomeBreakdownTypeOrStr | None = Field(alias="type")
    """The type of income. Possible values include:
      ``"regular"``: regular income
      ``"overtime"``: overtime income
      ``"bonus"``: bonus income"""

    rate: float | None
    """The hourly rate at which the income is paid."""

    hours: float | None
    """The number of hours logged for this income for this pay period."""

    total: float | None
    """The total pay for this pay period."""


class IncomeBreakdownDict(TypedDict):
    type_: IncomeBreakdownTypeOrStr | None
    rate: float | None
    hours: float | None
    total: float | None
