from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.signal_decision_outcome import SignalDecisionOutcomeOrStr
from .enums.signal_payment_method import SignalPaymentMethodOrStr


class ProcessorSignalDecisionReportRequest(SdkBaseModel):
    """ProcessorSignalDecisionReportRequest defines the request schema for ``/processor/signal/decision/report``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    processor_token: str
    """The processor token obtained from the Plaid integration partner. Processor tokens are in the format:
    ``processor-<environment>-<identifier>``"""

    client_transaction_id: str
    """Must be the same as the ``client_transaction_id`` supplied when calling ``/processor/signal/evaluate``"""

    initiated: bool
    """``true`` if the ACH transaction was initiated, ``false`` otherwise.

    This field must be returned as a boolean. If formatted incorrectly, this will result in an
    https://plaid.com/docs/errors/invalid-request/#invalid_field error."""

    days_funds_on_hold: OptionalNullable[int] = UNSET
    """The actual number of days (hold time) since the ACH debit transaction that you wait before making funds available
    to your customers. The holding time could affect the ACH return rate.

    For example, use 0 if you make funds available to your customers instantly or the same day following the debit
    transaction, or 1 if you make funds available the next day following the debit initialization."""

    decision_outcome: OptionalNullable[SignalDecisionOutcomeOrStr] = UNSET
    """The payment decision from the risk assessment.

    ``APPROVE``: approve the transaction without requiring further actions from your customers. For example, use this
    field if you are placing a standard hold for all the approved transactions before making funds available to your
    customers. You should also use this field if you decide to accelerate the fund availability for your customers.

    ``REVIEW``: the transaction requires manual review

    ``REJECT``: reject the transaction

    ``TAKE_OTHER_RISK_MEASURES``: for example, placing a longer hold on funds than those approved transactions or
    introducing customer frictions such as step-up verification/authentication

    ``NOT_EVALUATED``: if only logging the results without using them"""

    payment_method: OptionalNullable[SignalPaymentMethodOrStr] = UNSET
    """The payment method to complete the transaction after the risk assessment. It may be different from the default
    payment method.

    ``SAME_DAY_ACH``: Same Day ACH by Nacha. The debit transaction is processed and settled on the same day.

    ``STANDARD_ACH``: Standard ACH by Nacha.

    ``MULTIPLE_PAYMENT_METHODS``: if there is no default debit rail or there are multiple payment methods."""

    amount_instantly_available: OptionalNullable[float] = UNSET
    """The amount (in USD) made available to your customers instantly following the debit transaction. It could be a
    partial amount of the requested transaction (example: 102.05)."""


class ProcessorSignalDecisionReportRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    processor_token: str
    client_transaction_id: str
    initiated: bool
    days_funds_on_hold: NotRequired[int | None]
    decision_outcome: NotRequired[SignalDecisionOutcomeOrStr | None]
    payment_method: NotRequired[SignalPaymentMethodOrStr | None]
    amount_instantly_available: NotRequired[float | None]
