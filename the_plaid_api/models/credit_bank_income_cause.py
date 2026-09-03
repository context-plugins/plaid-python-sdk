from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.credit_bank_income_error_type import CreditBankIncomeErrorTypeOrStr


class CreditBankIncomeCause(SdkBaseModel):
    """An error object and associated ``item_id`` used to identify a specific Item and error when a batch operation
    operating on multiple Items has encountered an error in one of the Items."""

    error_type: CreditBankIncomeErrorTypeOrStr
    """A broad categorization of the error. Safe for programmatic use."""

    error_code: str
    """We use standard HTTP response codes for success and failure notifications, and our errors are further classified
    by ``error_type``. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related
    failures, and 50X codes are for Plaid-related issues. Error fields will be ``null`` if no error has occurred."""

    error_message: str
    """A developer-friendly representation of the error code. This may change over time and is not safe for programmatic
    use."""

    display_message: str
    """A user-friendly representation of the error code. null if the error is not related to user action. This may
    change over time and is not safe for programmatic use."""

    item_id: str
    """The ``item_id`` of the Item associated with this warning."""


class CreditBankIncomeCauseDict(TypedDict):
    error_type: CreditBankIncomeErrorTypeOrStr
    error_code: str
    error_message: str
    display_message: str
    item_id: str
