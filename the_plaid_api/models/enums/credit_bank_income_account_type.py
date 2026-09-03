from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditBankIncomeAccountType(str, Enum):
    """The account type. This will always be ``depository``."""

    DEPOSITORY = "depository"

    __str__ = str.__str__


CreditBankIncomeAccountTypeOrStr: TypeAlias = Annotated[
    CreditBankIncomeAccountType | str, open_enum_validator(CreditBankIncomeAccountType)
]
