from __future__ import annotations

from typing_extensions import TypedDict

from ..core import Date, SdkBaseModel
from .credit_bank_employer import CreditBankEmployer, CreditBankEmployerDict


class CreditBankEmployment(SdkBaseModel):
    """Detailed information for the bank employment."""

    bank_employment_id: str
    """A unique identifier for the bank employment."""

    account_id: str
    """Plaid's unique identifier for the account."""

    employer: CreditBankEmployer
    """Object containing employer data."""

    latest_deposit_date: Date
    """The date of the most recent deposit from this employer."""

    earliest_deposit_date: Date
    """The date of the earliest deposit from this employer from within the period of the days requested."""


class CreditBankEmploymentDict(TypedDict):
    bank_employment_id: str
    account_id: str
    employer: CreditBankEmployerDict
    latest_deposit_date: Date
    earliest_deposit_date: Date
