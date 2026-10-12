from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_bank_employment_report import CreditBankEmploymentReport, CreditBankEmploymentReportDict


class CreditBankEmploymentGetResponse(SdkBaseModel):
    """CreditBankEmploymentGetResponse defines the response schema for ``/beta/credit/v1/bank_employment/get``."""

    bank_employment_reports: list[CreditBankEmploymentReport]
    """Bank Employment data. Each entry in the array will be a distinct bank employment report."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class CreditBankEmploymentGetResponseDict(TypedDict):
    bank_employment_reports: list[CreditBankEmploymentReportDict]
    request_id: str
