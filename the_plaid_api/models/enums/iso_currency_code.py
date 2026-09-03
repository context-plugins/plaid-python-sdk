from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IsoCurrencyCode(str, Enum):
    """An ISO-4217 currency code, used with e-wallets and transactions."""

    GBP = "GBP"
    EUR = "EUR"

    __str__ = str.__str__


IsoCurrencyCodeOrStr: TypeAlias = Annotated[IsoCurrencyCode | str, open_enum_validator(IsoCurrencyCode)]
