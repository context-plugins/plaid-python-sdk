from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AccountVerificationInsightsPreviousReturns(SdkBaseModel):
    """Information about known ACH returns for the account and routing number."""

    has_previous_administrative_return: bool
    """Indicates whether Plaid's data sources include a known administrative ACH return for this account and routing
    number."""


class AccountVerificationInsightsPreviousReturnsDict(TypedDict):
    has_previous_administrative_return: bool
