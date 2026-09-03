from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.transfer_authorization_risk_level import TransferAuthorizationRiskLevelOrStr
from .signal_warning import SignalWarning, SignalWarningDict


class TransferAuthorizationPaymentRisk(SdkBaseModel):
    """This object includes the scores and risk level. This response is offered as an add-on to
    ``/transfer/authorization/create``. To request access to these fields, please contact your Plaid account manager."""

    bank_initiated_return_score: int | None
    """A score from 1-99 that indicates the transaction return risk: a higher risk score suggests a higher return
    likelihood.

    The score evaluates the transaction return risk because an account is overdrawn or because an ineligible account is
    used and covers return codes: "R01", "R02", "R03", "R04", "R06", "R08", "R09", "R13", "R16", "R17", "R20", "R23".
    These returns have a turnaround time of 2 banking days."""

    customer_initiated_return_score: int | None
    """A score from 1-99 that indicates the transaction return risk: a higher risk score suggests a higher return
    likelihood.

    The score evaluates the transaction return risk of an unauthorized debit and covers return codes: "R05", "R07",
    "R10", "R11", "R29". These returns typically have a return time frame of up to 60 calendar days. During this period,
    customers of financial institutions can dispute a transaction as unauthorized."""

    risk_level: TransferAuthorizationRiskLevelOrStr | None
    """Comprises five risk categories (high risk, medium-high risk, medium risk, medium-low risk, low risk) based on the
    probability of return"""

    warnings: list[SignalWarning]
    """If bank information was not available to be used, this array contains warnings describing why bank data is
    missing. If you want to receive an API error instead of scores in the case of missing bank data, file a support
    ticket or contact your Plaid account manager."""


class TransferAuthorizationPaymentRiskDict(TypedDict):
    bank_initiated_return_score: int | None
    customer_initiated_return_score: int | None
    risk_level: TransferAuthorizationRiskLevelOrStr | None
    warnings: list[SignalWarning | SignalWarningDict]
