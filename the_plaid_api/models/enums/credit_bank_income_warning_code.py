from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditBankIncomeWarningCode(str, Enum):
    """The warning code identifies a specific kind of warning. ``IDENTITY_UNAVAILABLE``: Unable to extract identity for
    the Item ``TRANSACTIONS_UNAVAILABLE``: Unable to extract transactions for the Item ``ITEM_UNAPPROVED``: User exited
    flow before giving permission to share data for the Item ``REPORT_DELETED``: Report deleted due to customer or
    consumer request ``DATA_UNAVAILABLE``: No relevant data was found for the Item"""

    IDENTITY_UNAVAILABLE = "IDENTITY_UNAVAILABLE"
    TRANSACTIONS_UNAVAILABLE = "TRANSACTIONS_UNAVAILABLE"
    ITEM_UNAPPROVED = "ITEM_UNAPPROVED"
    REPORT_DELETED = "REPORT_DELETED"
    DATA_UNAVAILABLE = "DATA_UNAVAILABLE"

    __str__ = str.__str__


CreditBankIncomeWarningCodeOrStr: TypeAlias = Annotated[
    CreditBankIncomeWarningCode | str, open_enum_validator(CreditBankIncomeWarningCode)
]
