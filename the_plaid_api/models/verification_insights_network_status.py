from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class VerificationInsightsNetworkStatus(SdkBaseModel):
    """Status information about the account and routing number in the Plaid network."""

    has_numbers_match: bool
    """Indicates whether we found at least one matching account for the ACH account and routing number."""

    is_numbers_match_verified: bool
    """Indicates if at least one matching account for the ACH account and routing number is already verified."""


class VerificationInsightsNetworkStatusDict(TypedDict):
    has_numbers_match: bool
    is_numbers_match_verified: bool
