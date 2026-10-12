from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.risk_level import RiskLevelOrStr
from .synthetic_fraud import SyntheticFraud, SyntheticFraudDict


class RiskCheckSyntheticIdentity(SdkBaseModel):
    """Field containing the data used in determining the outcome of the synthetic identity risk check.

    Contains the following fields:

    ``score`` - A score from 0 to 100 indicating the likelihood that the user is a synthetic identity."""

    score: int
    """A score from 0 to 100 indicating the likelihood that the user is a synthetic identity."""

    risk_level: Optional[RiskLevelOrStr] = UNSET
    """Risk level for the given risk check type."""

    first_party_synthetic_fraud: OptionalNullable[SyntheticFraud] = UNSET
    """Field containing the data used in determining the outcome of a synthetic fraud risk check."""

    third_party_synthetic_fraud: OptionalNullable[SyntheticFraud] = UNSET
    """Field containing the data used in determining the outcome of a synthetic fraud risk check."""


class RiskCheckSyntheticIdentityDict(TypedDict):
    score: int
    risk_level: NotRequired[RiskLevelOrStr]
    first_party_synthetic_fraud: NotRequired[SyntheticFraudDict | None]
    third_party_synthetic_fraud: NotRequired[SyntheticFraudDict | None]
