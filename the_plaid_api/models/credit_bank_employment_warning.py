from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .credit_bank_income_cause import CreditBankIncomeCause, CreditBankIncomeCauseDict
from .enums.credit_bank_employment_warning_type import CreditBankEmploymentWarningTypeOrStr
from .enums.credit_bank_income_warning_code import CreditBankIncomeWarningCodeOrStr


class CreditBankEmploymentWarning(SdkBaseModel):
    """The warning associated with the data that was unavailable for the Bank Employment Report."""

    warning_type: CreditBankEmploymentWarningTypeOrStr
    """The warning type which will always be ``BANK_EMPLOYMENT_WARNING``."""

    warning_code: CreditBankIncomeWarningCodeOrStr
    """The warning code identifies a specific kind of warning. ``IDENTITY_UNAVAILABLE``: Unable to extract identity for
    the Item ``TRANSACTIONS_UNAVAILABLE``: Unable to extract transactions for the Item ``ITEM_UNAPPROVED``: User exited
    flow before giving permission to share data for the Item ``REPORT_DELETED``: Report deleted due to customer or
    consumer request ``DATA_UNAVAILABLE``: No relevant data was found for the Item"""

    cause: CreditBankIncomeCause
    """An error object and associated ``item_id`` used to identify a specific Item and error when a batch operation
    operating on multiple Items has encountered an error in one of the Items."""


class CreditBankEmploymentWarningDict(TypedDict):
    warning_type: CreditBankEmploymentWarningTypeOrStr
    warning_code: CreditBankIncomeWarningCodeOrStr
    cause: CreditBankIncomeCauseDict
