from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .risk_check_stolen_identity import RiskCheckStolenIdentity, RiskCheckStolenIdentityDict
from .risk_check_synthetic_identity import RiskCheckSyntheticIdentity, RiskCheckSyntheticIdentityDict


class RiskCheckIdentityAbuseSignals(SdkBaseModel):
    """Result summary object capturing abuse signals related to ``identity abuse``, e.g. stolen and synthetic identity
    fraud. These attributes are only available for US identities and some signals may not be available depending on what
    information was collected."""

    synthetic_identity: RiskCheckSyntheticIdentity | None
    """Field containing the data used in determining the outcome of the synthetic identity risk check.

    Contains the following fields:

    ``score`` - A score from 0 to 100 indicating the likelihood that the user is a synthetic identity."""

    stolen_identity: RiskCheckStolenIdentity | None
    """Field containing the data used in determining the outcome of the stolen identity risk check.

    Contains the following fields:

    ``score`` - A score from 0 to 100 indicating the likelihood that the user is a stolen identity."""


class RiskCheckIdentityAbuseSignalsDict(TypedDict):
    synthetic_identity: RiskCheckSyntheticIdentityDict | None
    stolen_identity: RiskCheckStolenIdentityDict | None
