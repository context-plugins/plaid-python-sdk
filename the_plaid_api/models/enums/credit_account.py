from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreditAccount(str, Enum):
    """A credit card type account."""

    CREDIT_CARD = "credit card"
    PAYPAL = "paypal"

    __str__ = str.__str__


CreditAccountOrStr: TypeAlias = Annotated[CreditAccount | str, open_enum_validator(CreditAccount)]
