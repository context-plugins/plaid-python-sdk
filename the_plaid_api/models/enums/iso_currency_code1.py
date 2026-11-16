from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IsoCurrencyCode1(str, Enum):
    """An ISO-4217 currency code."""

    USD = "USD"

    __str__ = str.__str__


IsoCurrencyCode1OrStr: TypeAlias = Annotated[IsoCurrencyCode1 | str, open_enum_validator(IsoCurrencyCode1)]
