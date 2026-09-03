from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditBankEmploymentWarningType(str, Enum):
    """The warning type which will always be ``BANK_EMPLOYMENT_WARNING``."""

    BANK_EMPLOYMENT_WARNING = "BANK_EMPLOYMENT_WARNING"

    __str__ = str.__str__


CreditBankEmploymentWarningTypeOrStr: TypeAlias = Annotated[
    CreditBankEmploymentWarningType | str, open_enum_validator(CreditBankEmploymentWarningType)
]
