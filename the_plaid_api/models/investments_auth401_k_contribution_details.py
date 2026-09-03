from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .investment_transaction import InvestmentTransaction, InvestmentTransactionDict


class InvestmentsAuth401KContributionDetails(SdkBaseModel):
    """Object containing information on contribution transactions for the 401k account. Note that the sum fields in this
    object represent the total of absolute contribution values."""

    last_contribution_transactions: list[InvestmentTransaction]
    """A list of the most recent contribution transactions for the 401k account. Includes all contributions made on the
    same day."""

    contribution_count_1m: int
    """Number of contribution transactions on this account, for the past month."""

    contribution_amount_1m: float
    """Sum of the contribution transactions on this account, for the past month."""

    contribution_count_6m: int
    """Number of contribution transactions on this account, for the past 6 months."""

    contribution_amount_6m: float
    """Sum of the contribution transactions on this account, for the past 6 months."""

    contribution_count_12m: int
    """Number of contribution transactions on this account, for the past 12 months."""

    contribution_amount_12m: float
    """Sum of the contribution transactions on this account, for the past 12 months."""


class InvestmentsAuth401KContributionDetailsDict(TypedDict):
    last_contribution_transactions: list[InvestmentTransaction | InvestmentTransactionDict]
    contribution_count_1m: int
    contribution_amount_1m: float
    contribution_count_6m: int
    contribution_amount_6m: float
    contribution_count_12m: int
    contribution_amount_12m: float
