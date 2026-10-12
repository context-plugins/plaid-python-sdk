from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .business_industry_prediction_nullable import (
    BusinessIndustryPredictionNullable,
    BusinessIndustryPredictionNullableDict,
)
from .enums.business_verification_status_risk_check import BusinessVerificationStatusRiskCheckOrStr


class BusinessRiskCheck(SdkBaseModel):
    """Results from the business risk assessment check"""

    status: BusinessVerificationStatusRiskCheckOrStr
    """Status of the business risk assessment check"""

    score: int
    """A score from 0 to 100 indicating the risk assessment for the business"""

    industry_prediction: BusinessIndustryPredictionNullable | None
    """Nullable industry prediction details."""


class BusinessRiskCheckDict(TypedDict):
    status: BusinessVerificationStatusRiskCheckOrStr
    score: int
    industry_prediction: BusinessIndustryPredictionNullableDict | None
