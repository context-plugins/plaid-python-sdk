from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .mortgage_interest_rate import MortgageInterestRate, MortgageInterestRateDict
from .mortgage_property_address import MortgagePropertyAddress, MortgagePropertyAddressDict


class MortgageLiability(SdkBaseModel):
    """Contains details about a mortgage account."""

    account_id: str
    """The ID of the account that this liability belongs to."""

    account_number: str | None
    """The account number of the loan."""

    current_late_fee: float | None
    """The current outstanding amount charged for late payment."""

    escrow_balance: float | None
    """Total amount held in escrow to pay taxes and insurance on behalf of the borrower."""

    has_pmi: bool | None
    """Indicates whether the borrower has private mortgage insurance in effect."""

    has_prepayment_penalty: bool | None
    """Indicates whether the borrower will pay a penalty for early payoff of mortgage."""

    interest_rate: MortgageInterestRate
    """Object containing metadata about the interest rate for the mortgage."""

    last_payment_amount: float | None
    """The amount of the last payment."""

    last_payment_date: Date | None
    """The date of the last payment. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format
    (YYYY-MM-DD)."""

    loan_type_description: str | None
    """Description of the type of loan, for example ``conventional``, ``fixed``, or ``variable``. This field is provided
    directly from the loan servicer and does not have an enumerated set of possible values."""

    loan_term: str | None
    """Full duration of mortgage as at origination (e.g. ``10 year``)."""

    maturity_date: Date | None
    """Original date on which mortgage is due in full. Dates are returned in an `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    next_monthly_payment: float | None
    """The amount of the next payment."""

    next_payment_due_date: Date | None
    """The due date for the next payment. Dates are returned in an `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format (YYYY-MM-DD)."""

    origination_date: Date | None
    """The date on which the loan was initially lent. Dates are returned in an `ISO 8601
    <https://wikipedia.org/wiki/ISO_8601>`__ format (YYYY-MM-DD)."""

    origination_principal_amount: float | None
    """The original principal balance of the mortgage."""

    past_due_amount: float | None
    """Amount of loan (principal + interest) past due for payment."""

    property_address: MortgagePropertyAddress
    """Object containing fields describing property address."""

    ytd_interest_paid: float | None
    """The year to date (YTD) interest paid."""

    ytd_principal_paid: float | None
    """The YTD principal paid."""


class MortgageLiabilityDict(TypedDict):
    account_id: str
    account_number: str | None
    current_late_fee: float | None
    escrow_balance: float | None
    has_pmi: bool | None
    has_prepayment_penalty: bool | None
    interest_rate: MortgageInterestRateDict
    last_payment_amount: float | None
    last_payment_date: Date | None
    loan_type_description: str | None
    loan_term: str | None
    maturity_date: Date | None
    next_monthly_payment: float | None
    next_payment_due_date: Date | None
    origination_date: Date | None
    origination_principal_amount: float | None
    past_due_amount: float | None
    property_address: MortgagePropertyAddressDict
    ytd_interest_paid: float | None
    ytd_principal_paid: float | None
