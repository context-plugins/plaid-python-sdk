from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditBankIncomeWarningType(str, Enum):
    """The warning type which will always be ``BANK_INCOME_WARNING``."""

    BANK_INCOME_WARNING = "BANK_INCOME_WARNING"

    __str__ = str.__str__


CreditBankIncomeWarningTypeOrStr: TypeAlias = Annotated[
    CreditBankIncomeWarningType | str, open_enum_validator(CreditBankIncomeWarningType)
]
