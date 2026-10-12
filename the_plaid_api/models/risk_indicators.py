from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .bank_penalties_indicators import BankPenaltiesIndicators, BankPenaltiesIndicatorsDict
from .gambling_indicators import GamblingIndicators, GamblingIndicatorsDict
from .loan_disbursements_indicators import LoanDisbursementsIndicators, LoanDisbursementsIndicatorsDict
from .loan_payments_indicators import LoanPaymentsIndicators, LoanPaymentsIndicatorsDict
from .negative_balance_insights import NegativeBalanceInsights, NegativeBalanceInsightsDict


class RiskIndicators(SdkBaseModel):
    """Risk indicators focus on providing signal on the possibility of a borrower defaulting on their loan repayments by
    providing data points related to its payment behavior, debt, and other relevant financial information, helping
    lenders gauge the level of risk involved in a certain operation."""

    bank_penalties: OptionalNullable[BankPenaltiesIndicators] = UNSET
    """Insights into bank penalties and fees, including overdraft fees, NSF fees, and other bank-imposed charges."""

    gambling: OptionalNullable[GamblingIndicators] = UNSET
    """Insights into gambling-related transactions, including frequency, amounts, and top merchants."""

    loan_disbursements: OptionalNullable[LoanDisbursementsIndicators] = UNSET
    """Insights into loan disbursement transactions received by the user, tracking incoming funds from loan
    providers."""

    loan_payments: OptionalNullable[LoanPaymentsIndicators] = UNSET
    """Insights into loan payment transactions made by the user, tracking outgoing payments to loan providers."""

    negative_balance: OptionalNullable[NegativeBalanceInsights] = UNSET
    """Insights into negative balance occurrences, including frequency, duration, and minimum balance details."""


class RiskIndicatorsDict(TypedDict):
    bank_penalties: NotRequired[BankPenaltiesIndicatorsDict | None]
    gambling: NotRequired[GamblingIndicatorsDict | None]
    loan_disbursements: NotRequired[LoanDisbursementsIndicatorsDict | None]
    loan_payments: NotRequired[LoanPaymentsIndicatorsDict | None]
    negative_balance: NotRequired[NegativeBalanceInsightsDict | None]
