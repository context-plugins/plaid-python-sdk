from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StudentLoanRepaymentModel(SdkBaseModel):
    """Student loan repayment information used to configure Sandbox test data for the Liabilities product"""

    type_: str = Field(alias="type")
    """The only currently supported value for this field is ``standard``."""

    non_repayment_months: float
    """Configures the number of months before repayment starts."""

    repayment_months: float
    """Configures the number of months of repayments before the loan is paid off."""


class StudentLoanRepaymentModelDict(TypedDict):
    type_: str
    non_repayment_months: float
    repayment_months: float
