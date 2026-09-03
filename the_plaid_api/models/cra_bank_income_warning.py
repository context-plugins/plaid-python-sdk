from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cra_bank_income_cause import CraBankIncomeCause, CraBankIncomeCauseDict
from .enums.cra_bank_income_warning_code import CraBankIncomeWarningCodeOrStr
from .enums.credit_bank_income_warning_type import CreditBankIncomeWarningTypeOrStr


class CraBankIncomeWarning(SdkBaseModel):
    """The warning associated with the data that was unavailable."""

    warning_type: Optional[CreditBankIncomeWarningTypeOrStr] = UNSET
    """The warning type which will always be ``BANK_INCOME_WARNING``."""

    warning_code: Optional[CraBankIncomeWarningCodeOrStr] = UNSET
    """The warning code identifies a specific kind of warning. ``IDENTITY_UNAVAILABLE``: Unable to extract identity for
    the Item ``TRANSACTIONS_UNAVAILABLE``: Unable to extract transactions for the Item ``REPORT_DELETED``: Report
    deleted due to customer or consumer request ``DATA_UNAVAILABLE``: No relevant data was found for the Item"""

    cause: Optional[CraBankIncomeCause] = UNSET
    """An error object and associated ``item_id`` used to identify a specific Item and error when a batch operation
    operating on multiple Items has encountered an error in one of the Items."""


class CraBankIncomeWarningDict(TypedDict):
    warning_type: NotRequired[CreditBankIncomeWarningTypeOrStr]
    warning_code: NotRequired[CraBankIncomeWarningCodeOrStr]
    cause: NotRequired[CraBankIncomeCause | CraBankIncomeCauseDict]
