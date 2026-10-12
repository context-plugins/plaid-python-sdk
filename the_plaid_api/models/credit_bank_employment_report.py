from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .credit_bank_employment_item import CreditBankEmploymentItem, CreditBankEmploymentItemDict
from .credit_bank_employment_warning import CreditBankEmploymentWarning, CreditBankEmploymentWarningDict


class CreditBankEmploymentReport(SdkBaseModel):
    """The report of the Bank Employment data for an end user."""

    bank_employment_report_id: str
    """The unique identifier associated with the Bank Employment Report."""

    generated_time: RFC3339DateTime
    """The time when the Bank Employment Report was generated, in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__
    format (e.g. "2018-04-12T03:32:11Z")."""

    days_requested: int
    """The number of days requested by the customer for the Bank Employment Report."""

    items: list[CreditBankEmploymentItem]
    """The list of Items in the report along with the associated metadata about the Item."""

    warnings: list[CreditBankEmploymentWarning]
    """If data from the Bank Employment report was unable to be retrieved, the warnings will contain information about
    the error that caused the data to be incomplete."""


class CreditBankEmploymentReportDict(TypedDict):
    bank_employment_report_id: str
    generated_time: RFC3339DateTime
    days_requested: int
    items: list[CreditBankEmploymentItemDict]
    warnings: list[CreditBankEmploymentWarningDict]
