from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.risk_level import RiskLevelOrStr


class RiskCheckStolenIdentity(SdkBaseModel):
    """Field containing the data used in determining the outcome of the stolen identity risk check.

    Contains the following fields:

    ``score`` - A score from 0 to 100 indicating the likelihood that the user is a stolen identity."""

    score: int
    """A score from 0 to 100 indicating the likelihood that the user is a stolen identity."""

    risk_level: Optional[RiskLevelOrStr] = UNSET
    """Risk level for the given risk check type."""


class RiskCheckStolenIdentityDict(TypedDict):
    score: int
    risk_level: NotRequired[RiskLevelOrStr]
