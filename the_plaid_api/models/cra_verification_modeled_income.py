from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cra_verification_income_values import CraVerificationIncomeValues, CraVerificationIncomeValuesDict


class CraVerificationModeledIncome(SdkBaseModel):
    """Modeled estimate of current income based on recently observed income transactions."""

    monthly: CraVerificationIncomeValues
    """Modeled income values for a given time period."""

    annual: CraVerificationIncomeValues
    """Modeled income values for a given time period."""


class CraVerificationModeledIncomeDict(TypedDict):
    monthly: CraVerificationIncomeValuesDict
    annual: CraVerificationIncomeValuesDict
