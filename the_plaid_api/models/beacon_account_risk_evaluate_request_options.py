from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BeaconAccountRiskEvaluateRequestOptions(SdkBaseModel):
    """An optional object to filter ``/beacon/account_risk/v1/evaluate`` results to a subset of the accounts on the
    linked Item."""

    account_ids: Optional[list[str]] = UNSET
    """An array of ``account_ids`` for the specific accounts to evaluate."""


class BeaconAccountRiskEvaluateRequestOptionsDict(TypedDict):
    account_ids: NotRequired[list[str]]
