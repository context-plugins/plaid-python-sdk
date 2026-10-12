from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_document_metadata import CreditDocumentMetadata, CreditDocumentMetadataDict
from .credit_pay_stub_deductions import CreditPayStubDeductions, CreditPayStubDeductionsDict
from .credit_pay_stub_earnings import CreditPayStubEarnings, CreditPayStubEarningsDict
from .credit_pay_stub_employee import CreditPayStubEmployee, CreditPayStubEmployeeDict
from .credit_pay_stub_employer import CreditPayStubEmployer, CreditPayStubEmployerDict
from .credit_pay_stub_net_pay import CreditPayStubNetPay, CreditPayStubNetPayDict
from .pay_stub_pay_period_details import PayStubPayPeriodDetails, PayStubPayPeriodDetailsDict


class CreditPayStub(SdkBaseModel):
    """An object representing an end user's pay stub."""

    deductions: CreditPayStubDeductions
    """An object with the deduction information found on a pay stub."""

    document_id: str | None
    """An identifier of the document referenced by the document metadata."""

    document_metadata: CreditDocumentMetadata
    """Object representing metadata pertaining to the document."""

    earnings: CreditPayStubEarnings
    """An object representing both a breakdown of earnings on a pay stub and the total earnings."""

    employee: CreditPayStubEmployee
    """Data about the employee."""

    employer: CreditPayStubEmployer
    """Information about the employer on the pay stub."""

    net_pay: CreditPayStubNetPay
    """An object representing information about the net pay amount on the pay stub."""

    pay_period_details: PayStubPayPeriodDetails
    """Details about the pay period."""


class CreditPayStubDict(TypedDict):
    deductions: CreditPayStubDeductionsDict
    document_id: str | None
    document_metadata: CreditDocumentMetadataDict
    earnings: CreditPayStubEarningsDict
    employee: CreditPayStubEmployeeDict
    employer: CreditPayStubEmployerDict
    net_pay: CreditPayStubNetPayDict
    pay_period_details: PayStubPayPeriodDetailsDict
