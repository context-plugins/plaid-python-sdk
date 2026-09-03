from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .credit_session_document_income_result import (
    CreditSessionDocumentIncomeResult,
    CreditSessionDocumentIncomeResultDict,
)
from .link_session_bank_income_result import LinkSessionBankIncomeResult, LinkSessionBankIncomeResultDict
from .link_session_cra_document_upload_result import (
    LinkSessionCraDocumentUploadResult,
    LinkSessionCraDocumentUploadResultDict,
)
from .link_session_cra_item_add_result import LinkSessionCraItemAddResult, LinkSessionCraItemAddResultDict
from .link_session_cra_update_result import LinkSessionCraUpdateResult, LinkSessionCraUpdateResultDict
from .link_session_item_add_result import LinkSessionItemAddResult, LinkSessionItemAddResultDict
from .link_session_payroll_income_result import LinkSessionPayrollIncomeResult, LinkSessionPayrollIncomeResultDict


class LinkSessionResults(SdkBaseModel):
    """The set of results for a Link session."""

    item_add_results: list[LinkSessionItemAddResult]
    """The set of Item adds for the Link session. If you are not receiving this field and are instead receiving the
    deprecated ``on_success`` field, contact your account manager to update your integration."""

    cra_item_add_results: list[LinkSessionCraItemAddResult]
    """The set of Plaid Check Item adds for the Link session."""

    cra_update_results: list[LinkSessionCraUpdateResult]
    """The set of Plaid Check Item updates for the Link session."""

    bank_income_results: list[LinkSessionBankIncomeResult]
    """The set of bank income verifications for the Link session."""

    payroll_income_results: list[LinkSessionPayrollIncomeResult]
    """The set of payroll income verifications for the Link session."""

    document_income_results: CreditSessionDocumentIncomeResult | None
    """The details of a document income verification in Link"""

    cra_document_upload_results: OptionalNullable[LinkSessionCraDocumentUploadResult] = UNSET
    """The details of a document upload CRA session in Link"""


class LinkSessionResultsDict(TypedDict):
    item_add_results: list[LinkSessionItemAddResult | LinkSessionItemAddResultDict]
    cra_item_add_results: list[LinkSessionCraItemAddResult | LinkSessionCraItemAddResultDict]
    cra_update_results: list[LinkSessionCraUpdateResult | LinkSessionCraUpdateResultDict]
    bank_income_results: list[LinkSessionBankIncomeResult | LinkSessionBankIncomeResultDict]
    payroll_income_results: list[LinkSessionPayrollIncomeResult | LinkSessionPayrollIncomeResultDict]
    document_income_results: CreditSessionDocumentIncomeResult | CreditSessionDocumentIncomeResultDict | None
    cra_document_upload_results: NotRequired[
        LinkSessionCraDocumentUploadResult | LinkSessionCraDocumentUploadResultDict | None
    ]
