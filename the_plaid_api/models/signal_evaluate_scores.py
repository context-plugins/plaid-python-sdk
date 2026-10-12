from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_initiated_return_risk import BankInitiatedReturnRisk, BankInitiatedReturnRiskDict
from .customer_initiated_return_risk import CustomerInitiatedReturnRisk, CustomerInitiatedReturnRiskDict


class SignalEvaluateScores(SdkBaseModel):
    """Risk scoring details broken down by risk category. When using a Balance-only ruleset, this object will not be
    returned."""

    customer_initiated_return_risk: Optional[CustomerInitiatedReturnRisk] = UNSET
    """The object contains a risk score and a risk tier that evaluate the transaction return risk of an unauthorized
    debit. Common return codes in this category include: "R05", "R07", "R10", "R11", "R29". These returns typically have
    a return time frame of up to 60 calendar days. During this period, customers of financial institutions can dispute a
    transaction as unauthorized."""

    bank_initiated_return_risk: Optional[BankInitiatedReturnRisk] = UNSET
    """The object contains a risk score and a risk tier that evaluate the transaction return risk because an account is
    overdrawn or because an ineligible account is used. Common return codes in this category include: "R01", "R02",
    "R03", "R04", "R06", "R08", "R09", "R13", "R16", "R17", "R20", "R23". These returns have a turnaround time of 2
    banking days."""


class SignalEvaluateScoresDict(TypedDict):
    customer_initiated_return_risk: NotRequired[CustomerInitiatedReturnRiskDict]
    bank_initiated_return_risk: NotRequired[BankInitiatedReturnRiskDict]
