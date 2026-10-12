from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .investments_auth401_k_contribution_details import (
    InvestmentsAuth401KContributionDetails,
    InvestmentsAuth401KContributionDetailsDict,
)
from .investments_auth401_k_fee_details import InvestmentsAuth401KFeeDetails, InvestmentsAuth401KFeeDetailsDict


class InvestmentsAuthAccountDetails401K(SdkBaseModel):
    """Additional account fee and contribution information for 401k type accounts."""

    account_id: Optional[str] = UNSET
    """The ID of the 401k account."""

    fee_details: Optional[InvestmentsAuth401KFeeDetails] = UNSET
    """Object containing information on account fee transactions for the 401k account."""

    contribution_details: Optional[InvestmentsAuth401KContributionDetails] = UNSET
    """Object containing information on contribution transactions for the 401k account. Note that the sum fields in this
    object represent the total of absolute contribution values."""


class InvestmentsAuthAccountDetails401KDict(TypedDict):
    account_id: NotRequired[str]
    fee_details: NotRequired[InvestmentsAuth401KFeeDetailsDict]
    contribution_details: NotRequired[InvestmentsAuth401KContributionDetailsDict]
