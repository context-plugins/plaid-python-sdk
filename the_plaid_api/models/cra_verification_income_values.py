from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CraVerificationIncomeValues(SdkBaseModel):
    """Modeled income values for a given time period."""

    gross_income: float
    """Gross Income modeled from trends of observed transactions."""

    net_income: float
    """Net Income estimated from observed transactions."""


class CraVerificationIncomeValuesDict(TypedDict):
    gross_income: float
    net_income: float
