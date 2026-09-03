from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .account_verification_insights_previous_returns import (
    AccountVerificationInsightsPreviousReturns,
    AccountVerificationInsightsPreviousReturnsDict,
)
from .enums.verification_insights_account_number_format import VerificationInsightsAccountNumberFormatOrStr
from .verification_insights_network_status import (
    VerificationInsightsNetworkStatus,
    VerificationInsightsNetworkStatusDict,
)


class VerificationInsights(SdkBaseModel):
    """Insights from performing database verification for the account. Only returned for Auth Items using Database
    Auth."""

    name_match_score: OptionalNullable[int] = UNSET
    """Indicates the score of the name match between the given name provided during database verification (available in
    the https://plaid.com/docs/api/products/auth/#auth-get-response-accounts-verification-name field if using standard
    Database Auth, or provided in the request if using ``/auth/verify``) and matched Plaid network accounts. If defined,
    will be a value between 0 and 100. Will be undefined if name matching was not enabled for the database verification
    session or if there were no eligible Plaid network matches to compare the given name with."""

    network_status: VerificationInsightsNetworkStatus
    """Status information about the account and routing number in the Plaid network."""

    previous_returns: Optional[AccountVerificationInsightsPreviousReturns] = UNSET
    """Information about known ACH returns for the account and routing number."""

    account_number_format: VerificationInsightsAccountNumberFormatOrStr
    """Indicator of account number format validity for institution.

    ``valid``: indicates that the account number has a correct format for the institution.

    ``invalid``: indicates that the account number has an incorrect format for the institution.

    ``unknown``: indicates that there was not enough information to determine whether the format is correct for the
    institution."""


class VerificationInsightsDict(TypedDict):
    name_match_score: NotRequired[int | None]
    network_status: VerificationInsightsNetworkStatus | VerificationInsightsNetworkStatusDict
    previous_returns: NotRequired[
        AccountVerificationInsightsPreviousReturns | AccountVerificationInsightsPreviousReturnsDict
    ]
    account_number_format: VerificationInsightsAccountNumberFormatOrStr
