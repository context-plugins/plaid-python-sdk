from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraMonthlyIncomeValues(SdkBaseModel):
    """Modeled estimate of the monthly income."""

    gross_income: float
    """Gross Income modeled from trends of observed transactions."""

    net_income: float
    """Net Income estimated from observed transactions."""


class CraMonthlyIncomeValuesDict(TypedDict):
    gross_income: float
    net_income: float
