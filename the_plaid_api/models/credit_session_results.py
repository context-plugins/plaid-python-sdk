from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .credit_session_bank_employment_result import (
    CreditSessionBankEmploymentResult,
    CreditSessionBankEmploymentResultDict,
)
from .credit_session_bank_income_result import CreditSessionBankIncomeResult, CreditSessionBankIncomeResultDict
from .credit_session_document_income_result import (
    CreditSessionDocumentIncomeResult,
    CreditSessionDocumentIncomeResultDict,
)
from .credit_session_item_add_result import CreditSessionItemAddResult, CreditSessionItemAddResultDict
from .credit_session_payroll_income_result import CreditSessionPayrollIncomeResult, CreditSessionPayrollIncomeResultDict


class CreditSessionResults(SdkBaseModel):
    """The set of results for a Link session."""

    item_add_results: Optional[list[CreditSessionItemAddResult]] = UNSET
    """The set of Item adds for the Link session."""

    bank_income_results: Optional[list[CreditSessionBankIncomeResult]] = UNSET
    """The set of bank income verifications for the Link session."""

    bank_employment_results: Optional[list[CreditSessionBankEmploymentResult]] = UNSET
    """The set of bank employment verifications for the Link session."""

    payroll_income_results: Optional[list[CreditSessionPayrollIncomeResult]] = UNSET
    """The set of payroll income verifications for the Link session."""

    document_income_results: OptionalNullable[CreditSessionDocumentIncomeResult] = UNSET
    """The details of a document income verification in Link"""


class CreditSessionResultsDict(TypedDict):
    item_add_results: NotRequired[list[CreditSessionItemAddResultDict]]
    bank_income_results: NotRequired[list[CreditSessionBankIncomeResultDict]]
    bank_employment_results: NotRequired[list[CreditSessionBankEmploymentResultDict]]
    payroll_income_results: NotRequired[list[CreditSessionPayrollIncomeResultDict]]
    document_income_results: NotRequired[CreditSessionDocumentIncomeResultDict | None]
