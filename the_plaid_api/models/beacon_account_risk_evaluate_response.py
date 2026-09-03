from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .beacon_account_risk_evaluate_account import BeaconAccountRiskEvaluateAccount, BeaconAccountRiskEvaluateAccountDict


class BeaconAccountRiskEvaluateResponse(SdkBaseModel):
    """BeaconAccountRiskEvaluateResponse defines the response schema for ``/beacon/account_risk/v1/evaluate``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""

    accounts: list[BeaconAccountRiskEvaluateAccount]
    """The accounts for which a risk evaluation has been requested."""


class BeaconAccountRiskEvaluateResponseDict(TypedDict):
    request_id: str
    accounts: list[BeaconAccountRiskEvaluateAccount | BeaconAccountRiskEvaluateAccountDict]
