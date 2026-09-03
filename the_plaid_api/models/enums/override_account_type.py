from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OverrideAccountType(str, Enum):
    """``investment:`` Investment account.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``payroll:`` Payroll account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    INVESTMENT = "investment"
    CREDIT = "credit"
    DEPOSITORY = "depository"
    LOAN = "loan"
    PAYROLL = "payroll"
    OTHER = "other"

    __str__ = str.__str__


OverrideAccountTypeOrStr: TypeAlias = Annotated[OverrideAccountType | str, open_enum_validator(OverrideAccountType)]
