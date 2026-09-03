from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.risk_level import RiskLevelOrStr


class RiskCheckNetwork(SdkBaseModel):
    """Result summary object specifying values for network attributes of risk check."""

    risk_level: RiskLevelOrStr
    """Risk level for the given risk check type."""

    factors: list[str]
    """List of factors, when available, that contribute towards the risk level of the given risk check type."""


class RiskCheckNetworkDict(TypedDict):
    risk_level: RiskLevelOrStr
    factors: list[str]
