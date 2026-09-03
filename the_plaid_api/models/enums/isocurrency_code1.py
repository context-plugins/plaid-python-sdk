from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class IsocurrencyCode1(str, Enum):
    """An ISO-4217 currency code."""

    USD = "USD"

    __str__ = str.__str__


IsocurrencyCode1OrStr: TypeAlias = Annotated[IsocurrencyCode1 | str, open_enum_validator(IsocurrencyCode1)]
