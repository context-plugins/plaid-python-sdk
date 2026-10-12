from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loan_payments_counts import LoanPaymentsCounts, LoanPaymentsCountsDict
from .loan_payments_merchant_counts import LoanPaymentsMerchantCounts, LoanPaymentsMerchantCountsDict


class MonitoringLoanInsights(SdkBaseModel):
    """An object representing the loan exposure subcategory of the report"""

    loan_payments_counts: LoanPaymentsCounts
    """Details regarding the number of loan payments"""

    loan_disbursements_count: float
    """The number of loan disbursements detected in the last 30 days"""

    loan_payment_merchants_counts: LoanPaymentsMerchantCounts
    """Details regarding the number of unique loan payment merchants"""


class MonitoringLoanInsightsDict(TypedDict):
    loan_payments_counts: LoanPaymentsCountsDict
    loan_disbursements_count: float
    loan_payment_merchants_counts: LoanPaymentsMerchantCountsDict
