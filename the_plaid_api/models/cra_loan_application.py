from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel
from .enums.cra_loan_application_decision import CraLoanApplicationDecisionOrStr
from .enums.cra_loan_type import CraLoanTypeOrStr


class CraLoanApplication(SdkBaseModel):
    """Contains loan application data."""

    user_token: str
    """The user token for the user associated with the loan."""

    application_id: str
    """A unique identifier for the loan application. Personally identifiable information, such as an email address or
    phone number, should not be used in the ``application_id``."""

    type_: CraLoanTypeOrStr = Field(alias="type")
    """The type of loan the user applied for."""

    decision: CraLoanApplicationDecisionOrStr
    """The decision of the loan application."""

    application_date: Optional[Date] = UNSET
    """The date the user applied for the loan. The date should be in ISO 8601 format (YYYY-MM-DD)."""

    decision_date: Optional[Date] = UNSET
    """The date when the loan application's decision was made. The date should be in ISO 8601 format (YYYY-MM-DD)."""


class CraLoanApplicationDict(TypedDict):
    user_token: str
    application_id: str
    type_: CraLoanTypeOrStr
    decision: CraLoanApplicationDecisionOrStr
    application_date: NotRequired[Date]
    decision_date: NotRequired[Date]
