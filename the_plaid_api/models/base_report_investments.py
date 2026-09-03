from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .base_report_investment_holding import BaseReportInvestmentHolding, BaseReportInvestmentHoldingDict
from .base_report_investment_security import BaseReportInvestmentSecurity, BaseReportInvestmentSecurityDict
from .base_report_investment_transaction import BaseReportInvestmentTransaction, BaseReportInvestmentTransactionDict


class BaseReportInvestments(SdkBaseModel):
    """A set of fields describing the investments data on an account."""

    holdings: list[BaseReportInvestmentHolding]
    """Quantities and values of securities held in the investment account. Map to the ``securities`` array for security
    details."""

    securities: list[BaseReportInvestmentSecurity]
    """Details of specific securities held in the investment account."""

    investment_transactions: list[BaseReportInvestmentTransaction]
    """Transaction history on the investment account."""


class BaseReportInvestmentsDict(TypedDict):
    holdings: list[BaseReportInvestmentHolding | BaseReportInvestmentHoldingDict]
    securities: list[BaseReportInvestmentSecurity | BaseReportInvestmentSecurityDict]
    investment_transactions: list[BaseReportInvestmentTransaction | BaseReportInvestmentTransactionDict]
