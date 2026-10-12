from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, OptionalNullable, SdkBaseModel
from .pslfstatus import Pslfstatus, PslfstatusDict
from .servicer_address_data import ServicerAddressData, ServicerAddressDataDict
from .student_loan_status import StudentLoanStatus, StudentLoanStatusDict
from .student_repayment_plan import StudentRepaymentPlan, StudentRepaymentPlanDict


class StudentLoan(SdkBaseModel):
    """Contains details about a student loan account"""

    account_id: str | None
    """The ID of the account that this liability belongs to. Each account can only contain one liability."""

    account_number: str | None
    """The account number of the loan. For some institutions, this may be a masked version of the number (e.g., the last
    4 digits instead of the entire number)."""

    disbursement_dates: list[Date] | None
    """The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are
    returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    expected_payoff_date: Date | None
    """The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are
    returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    guarantor: str | None
    """The guarantor of the student loan."""

    interest_rate_percentage: float
    """The interest rate on the loan as a percentage."""

    is_overdue: bool | None
    """``true`` if a payment is currently overdue. Availability for this field is limited."""

    last_payment_amount: float | None
    """The amount of the last payment."""

    last_payment_date: Date | None
    """The date of the last payment. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (YYYY-MM-DD)."""

    last_statement_balance: OptionalNullable[float] = UNSET
    """The total amount owed as of the last statement issued"""

    last_statement_issue_date: Date | None
    """The date of the last statement. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format (YYYY-MM-DD)."""

    loan_name: str | None
    """The type of loan, e.g., "Consolidation Loans"."""

    loan_status: StudentLoanStatus
    """An object representing the status of the student loan"""

    minimum_payment_amount: float | None
    """The minimum payment due for the next billing cycle. There are some exceptions: Some institutions require a
    minimum payment across all loans associated with an account number. Our API presents that same minimum payment
    amount on each loan. The institutions that do this are: Great Lakes ( ``ins_116861``), Firstmark (``ins_116295``),
    Commonbond Firstmark Services (``ins_116950``), Granite State (``ins_116308``), and Oklahoma Student Loan Authority
    (``ins_116945``). Firstmark (``ins_116295`` ) and Navient (``ins_116248``) will display as $0 if there is an autopay
    program in effect."""

    next_payment_due_date: Date | None
    """The due date for the next payment. The due date is ``null`` if a payment is not expected. A payment is not
    expected if ``loan_status.type`` is ``deferment``, ``in school``, ``consolidated``, ``paid in full``, or
    ``transferred``. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    origination_date: Date | None
    """The date on which the loan was initially lent. Dates are returned in an `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    origination_principal_amount: float | None
    """The original principal balance of the loan."""

    outstanding_interest_amount: float | None
    """The total dollar amount of the accrued interest balance. For Sallie Mae ( ``ins_116944``), this amount is
    included in the current balance of the loan, so this field will return as ``null``."""

    payment_reference_number: str | None
    """The relevant account number that should be used to reference this loan for payments. In the majority of cases,
    ``payment_reference_number`` will match ``account_number``, but in some institutions, such as Great Lakes
    (``ins_116861``), it will be different."""

    pslf_status: Pslfstatus
    """Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned
    if the institution is FedLoan (``ins_116527``). Since FedLoan no longer services student loans, this field is no
    longer returned."""

    repayment_plan: StudentRepaymentPlan
    """An object representing the repayment plan for the student loan"""

    sequence_number: str | None
    """The sequence number of the student loan. Heartland ECSI (``ins_116948``) does not make this field available."""

    servicer_address: ServicerAddressData
    """The address of the student loan servicer. This is generally the remittance address to which payments should be
    sent."""

    ytd_interest_paid: float | None
    """The year to date (YTD) interest paid. Availability for this field is limited."""

    ytd_principal_paid: float | None
    """The year to date (YTD) principal paid. Availability for this field is limited."""


class StudentLoanDict(TypedDict):
    account_id: str | None
    account_number: str | None
    disbursement_dates: list[Date] | None
    expected_payoff_date: Date | None
    guarantor: str | None
    interest_rate_percentage: float
    is_overdue: bool | None
    last_payment_amount: float | None
    last_payment_date: Date | None
    last_statement_balance: NotRequired[float | None]
    last_statement_issue_date: Date | None
    loan_name: str | None
    loan_status: StudentLoanStatusDict
    minimum_payment_amount: float | None
    next_payment_due_date: Date | None
    origination_date: Date | None
    origination_principal_amount: float | None
    outstanding_interest_amount: float | None
    payment_reference_number: str | None
    pslf_status: PslfstatusDict
    repayment_plan: StudentRepaymentPlanDict
    sequence_number: str | None
    servicer_address: ServicerAddressDataDict
    ytd_interest_paid: float | None
    ytd_principal_paid: float | None
