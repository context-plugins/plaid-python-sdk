from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_annual_income_values import CraAnnualIncomeValues, CraAnnualIncomeValuesDict
from .cra_monthly_income_values import CraMonthlyIncomeValues, CraMonthlyIncomeValuesDict


class CraCurrentModeledIncome(SdkBaseModel):
    """Modeled estimate of current income based on recently observed income transactions."""

    monthly: CraMonthlyIncomeValues
    """Modeled estimate of the monthly income."""

    annual: CraAnnualIncomeValues
    """Modeled estimate of the annual income."""


class CraCurrentModeledIncomeDict(TypedDict):
    monthly: CraMonthlyIncomeValuesDict
    annual: CraAnnualIncomeValuesDict
