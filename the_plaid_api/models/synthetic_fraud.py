from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.risk_level import RiskLevelOrStr


class SyntheticFraud(SdkBaseModel):
    """Field containing the data used in determining the outcome of a synthetic fraud risk check."""

    risk_level: RiskLevelOrStr
    """Risk level for the given risk check type."""


class SyntheticFraudDict(TypedDict):
    risk_level: RiskLevelOrStr
