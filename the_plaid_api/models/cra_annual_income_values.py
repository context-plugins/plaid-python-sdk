from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraAnnualIncomeValues(SdkBaseModel):
    """Modeled estimate of the annual income."""

    gross_income: float
    """Gross Income modeled from trends of observed transactions."""

    net_income: float
    """Net Income estimated from observed transactions."""


class CraAnnualIncomeValuesDict(TypedDict):
    gross_income: float
    net_income: float
