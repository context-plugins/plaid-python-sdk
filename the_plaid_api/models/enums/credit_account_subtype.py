from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditAccountSubtype(str, Enum):
    """Valid account subtypes for credit accounts. For a list containing descriptions of each subtype, see `Account
    schemas <https://plaid.com/docs/api/accounts/#StandaloneAccountType-credit>`__."""

    CREDIT_CARD = "credit card"
    PAYPAL = "paypal"
    ALL = "all"

    __str__ = str.__str__


CreditAccountSubtypeOrStr: TypeAlias = Annotated[CreditAccountSubtype | str, open_enum_validator(CreditAccountSubtype)]
