from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .credit_bank_income_cause import CreditBankIncomeCause, CreditBankIncomeCauseDict
from .enums.credit_bank_income_warning_code import CreditBankIncomeWarningCodeOrStr
from .enums.credit_bank_income_warning_type import CreditBankIncomeWarningTypeOrStr


class CreditBankIncomeWarning(SdkBaseModel):
    """The warning associated with the data that was unavailable for the Bank Income Report."""

    warning_type: Optional[CreditBankIncomeWarningTypeOrStr] = UNSET
    """The warning type which will always be ``BANK_INCOME_WARNING``."""

    warning_code: Optional[CreditBankIncomeWarningCodeOrStr] = UNSET
    """The warning code identifies a specific kind of warning. ``IDENTITY_UNAVAILABLE``: Unable to extract identity for
    the Item ``TRANSACTIONS_UNAVAILABLE``: Unable to extract transactions for the Item ``ITEM_UNAPPROVED``: User exited
    flow before giving permission to share data for the Item ``REPORT_DELETED``: Report deleted due to customer or
    consumer request ``DATA_UNAVAILABLE``: No relevant data was found for the Item"""

    cause: Optional[CreditBankIncomeCause] = UNSET
    """An error object and associated ``item_id`` used to identify a specific Item and error when a batch operation
    operating on multiple Items has encountered an error in one of the Items."""


class CreditBankIncomeWarningDict(TypedDict):
    warning_type: NotRequired[CreditBankIncomeWarningTypeOrStr]
    warning_code: NotRequired[CreditBankIncomeWarningCodeOrStr]
    cause: NotRequired[CreditBankIncomeCause | CreditBankIncomeCauseDict]
