from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AccountType(str, Enum):
    """``investment:`` Investment account. In API versions 2018-05-22 and earlier, this type is called ``brokerage``
    instead.

    ``credit:`` Credit card

    ``depository:`` Depository account

    ``loan:`` Loan account

    ``other:`` Non-specified account type

    See the `Account type schema <https://plaid.com/docs/api/accounts#account-type-schema>`__ for a full listing of
    account types and corresponding subtypes."""

    INVESTMENT = "investment"
    CREDIT = "credit"
    DEPOSITORY = "depository"
    LOAN = "loan"
    BROKERAGE = "brokerage"
    OTHER = "other"

    __str__ = str.__str__


AccountTypeOrStr: TypeAlias = Annotated[AccountType | str, open_enum_validator(AccountType)]
