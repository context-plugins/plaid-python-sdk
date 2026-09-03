from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraBankIncomeWarningCode(str, Enum):
    """The warning code identifies a specific kind of warning. ``IDENTITY_UNAVAILABLE``: Unable to extract identity for
    the Item ``TRANSACTIONS_UNAVAILABLE``: Unable to extract transactions for the Item ``REPORT_DELETED``: Report
    deleted due to customer or consumer request ``DATA_UNAVAILABLE``: No relevant data was found for the Item"""

    IDENTITY_UNAVAILABLE = "IDENTITY_UNAVAILABLE"
    TRANSACTIONS_UNAVAILABLE = "TRANSACTIONS_UNAVAILABLE"
    REPORT_DELETED = "REPORT_DELETED"
    DATA_UNAVAILABLE = "DATA_UNAVAILABLE"

    __str__ = str.__str__


CraBankIncomeWarningCodeOrStr: TypeAlias = Annotated[
    CraBankIncomeWarningCode | str, open_enum_validator(CraBankIncomeWarningCode)
]
