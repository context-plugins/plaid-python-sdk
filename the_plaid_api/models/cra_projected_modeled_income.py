from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_annual_income_values import CraAnnualIncomeValues, CraAnnualIncomeValuesDict
from .cra_monthly_income_values import CraMonthlyIncomeValues, CraMonthlyIncomeValuesDict


class CraProjectedModeledIncome(SdkBaseModel):
    """Forward-looking modeled estimate of income based on recent income transactions and trends in active streams."""

    monthly: CraMonthlyIncomeValues
    """Modeled estimate of the monthly income."""

    annual: CraAnnualIncomeValues
    """Modeled estimate of the annual income."""


class CraProjectedModeledIncomeDict(TypedDict):
    monthly: CraMonthlyIncomeValuesDict
    annual: CraAnnualIncomeValuesDict
