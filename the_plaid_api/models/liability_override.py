from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .address import Address, AddressDict
from .pslfstatus import Pslfstatus, PslfstatusDict
from .student_loan_repayment_model import StudentLoanRepaymentModel, StudentLoanRepaymentModelDict
from .student_loan_status import StudentLoanStatus, StudentLoanStatusDict


class LiabilityOverride(SdkBaseModel):
    """Used to configure Sandbox test data for the Liabilities product"""

    type_: str = Field(alias="type")
    """The type of the liability object, either ``credit`` or ``student``. Mortgages are not currently supported in the
    custom Sandbox."""

    purchase_apr: float
    """The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest
    charges. Can only be set if ``type`` is ``credit``."""

    cash_apr: float
    """The cash APR percentage value. Can only be set if ``type`` is ``credit``."""

    balance_transfer_apr: float
    """The balance transfer APR percentage value. Can only be set if ``type`` is ``credit``."""

    special_apr: float
    """The special APR percentage value. Can only be set if ``type`` is ``credit``."""

    last_payment_amount: float
    """Override the ``last_payment_amount`` field. Can only be set if ``type`` is ``credit``."""

    minimum_payment_amount: float
    """Override the ``minimum_payment_amount`` field. Can only be set if ``type`` is ``credit`` or ``student``."""

    is_overdue: bool
    """Override the ``is_overdue`` field"""

    origination_date: Date
    """The date on which the loan was initially lent, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ (YYYY-MM-DD)
    format. Can only be set if ``type`` is ``student``."""

    principal: float
    """The original loan principal. Can only be set if ``type`` is ``student``."""

    nominal_apr: float
    """The interest rate on the loan as a percentage. Can only be set if ``type`` is ``student``."""

    interest_capitalization_grace_period_months: float
    """If set, interest capitalization begins at the given number of months after loan origination. By default interest
    is never capitalized. Can only be set if ``type`` is ``student``."""

    repayment_model: StudentLoanRepaymentModel
    """Student loan repayment information used to configure Sandbox test data for the Liabilities product"""

    expected_payoff_date: Date
    """Override the ``expected_payoff_date`` field. Can only be set if ``type`` is ``student``."""

    guarantor: str
    """Override the ``guarantor`` field. Can only be set if ``type`` is ``student``."""

    is_federal: bool
    """Override the ``is_federal`` field. Can only be set if ``type`` is ``student``."""

    loan_name: str
    """Override the ``loan_name`` field. Can only be set if ``type`` is ``student``."""

    loan_status: StudentLoanStatus
    """An object representing the status of the student loan"""

    payment_reference_number: str
    """Override the ``payment_reference_number`` field. Can only be set if ``type`` is ``student``."""

    pslf_status: Pslfstatus
    """Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned
    if the institution is FedLoan (``ins_116527``). Since FedLoan no longer services student loans, this field is no
    longer returned."""

    repayment_plan_description: str
    """Override the ``repayment_plan.description`` field. Can only be set if ``type`` is ``student``."""

    repayment_plan_type: str
    """Override the ``repayment_plan.type`` field. Can only be set if ``type`` is ``student``. Possible values are:
    ``"extended graduated"``, ``"extended standard"``, ``"graduated"``, ``"income-contingent repayment"``,
    ``"income-based repayment"``, ``"income-sensitive repayment"``, ``"interest only"``, ``"other"``, ``"pay as you
    earn"``, ``"revised pay as you earn"``, ``"standard"``, or ``"saving on a valuable education"``."""

    sequence_number: str
    """Override the ``sequence_number`` field. Can only be set if ``type`` is ``student``."""

    servicer_address: Address
    """A physical mailing address."""


class LiabilityOverrideDict(TypedDict):
    type_: str
    purchase_apr: float
    cash_apr: float
    balance_transfer_apr: float
    special_apr: float
    last_payment_amount: float
    minimum_payment_amount: float
    is_overdue: bool
    origination_date: Date
    principal: float
    nominal_apr: float
    interest_capitalization_grace_period_months: float
    repayment_model: StudentLoanRepaymentModelDict
    expected_payoff_date: Date
    guarantor: str
    is_federal: bool
    loan_name: str
    loan_status: StudentLoanStatusDict
    payment_reference_number: str
    pslf_status: PslfstatusDict
    repayment_plan_description: str
    repayment_plan_type: str
    sequence_number: str
    servicer_address: AddressDict
