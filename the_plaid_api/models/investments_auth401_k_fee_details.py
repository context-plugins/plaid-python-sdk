from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InvestmentsAuth401KFeeDetails(SdkBaseModel):
    """Object containing information on account fee transactions for the 401k account."""

    account_fee_count_12m: int
    """Number of account fee transactions on this account, for the past 12 months."""

    account_fee_amount_12m: float
    """Sum of account fee transactions on this account, for the past 12 months."""


class InvestmentsAuth401KFeeDetailsDict(TypedDict):
    account_fee_count_12m: int
    account_fee_amount_12m: float
