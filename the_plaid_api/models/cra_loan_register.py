from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .cra_loan_opened_status import CraLoanOpenedStatus, CraLoanOpenedStatusDict
from .cra_loan_register_application import CraLoanRegisterApplication, CraLoanRegisterApplicationDict
from .enums.cra_loan_payment_schedule import CraLoanPaymentScheduleOrStr
from .enums.cra_loan_type import CraLoanTypeOrStr


class CraLoanRegister(SdkBaseModel):
    """Contains loan data to register."""

    user_token: str
    """The user token for the user associated with the loan."""

    loan_id: str
    """A unique identifier for the loan. Personally identifiable information, such as an email address or phone number,
    should not be used in the ``loan_id``."""

    type_: CraLoanTypeOrStr = Field(alias="type")
    """The type of loan the user applied for."""

    payment_schedule: CraLoanPaymentScheduleOrStr
    """The frequency of a loan's payment schedule. ``BIWEEKLY`` represents one payment every two weeks."""

    opened_date: Date
    """The date the loan account was opened. The date should be in ISO 8601 format (YYYY-MM-DD)."""

    opened_with_status: CraLoanOpenedStatus
    """Contains the status and date information of the loan when registering."""

    loan_amount: Optional[float] = UNSET
    """The total amount of the approved loan."""

    application: Optional[CraLoanRegisterApplication] = UNSET
    """Contains loan application data to register."""


class CraLoanRegisterDict(TypedDict):
    user_token: str
    loan_id: str
    type_: CraLoanTypeOrStr
    payment_schedule: CraLoanPaymentScheduleOrStr
    opened_date: Date
    opened_with_status: CraLoanOpenedStatusDict
    loan_amount: NotRequired[float]
    application: NotRequired[CraLoanRegisterApplicationDict]
