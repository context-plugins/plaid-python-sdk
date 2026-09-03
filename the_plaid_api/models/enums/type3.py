from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type3(str, Enum):
    """The type of the repayment plan."""

    EXTENDED_GRADUATED = "extended graduated"
    EXTENDED_STANDARD = "extended standard"
    GRADUATED = "graduated"
    INCOME_CONTINGENT_REPAYMENT = "income-contingent repayment"
    INCOME_BASED_REPAYMENT = "income-based repayment"
    INCOME_SENSITIVE_REPAYMENT = "income-sensitive repayment"
    INTEREST_ONLY = "interest only"
    OTHER = "other"
    PAY_AS_YOU_EARN = "pay as you earn"
    REVISED_PAY_AS_YOU_EARN = "revised pay as you earn"
    STANDARD = "standard"
    SAVING_ON_A_VALUABLE_EDUCATION = "saving on a valuable education"

    __str__ = str.__str__


Type3OrStr: TypeAlias = Annotated[Type3 | str, open_enum_validator(Type3)]
