from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_loan_payment_history import CraLoanPaymentHistory, CraLoanPaymentHistoryDict
from .cra_loan_status_history_update import CraLoanStatusHistoryUpdate, CraLoanStatusHistoryUpdateDict


class CraLoanUpdate(SdkBaseModel):
    """Contains loan data to update."""

    loan_id: Optional[str] = UNSET
    """A unique identifier for the loan. Personally identifiable information, such as an email address or phone number,
    should not be used in the ``loan_id``."""

    status_history: Optional[list[CraLoanStatusHistoryUpdate]] = UNSET
    """A list of status update history of the loan."""

    payment_history: Optional[list[CraLoanPaymentHistory]] = UNSET
    """The updates to the payment history for the loan."""


class CraLoanUpdateDict(TypedDict):
    loan_id: NotRequired[str]
    status_history: NotRequired[list[CraLoanStatusHistoryUpdate | CraLoanStatusHistoryUpdateDict]]
    payment_history: NotRequired[list[CraLoanPaymentHistory | CraLoanPaymentHistoryDict]]
