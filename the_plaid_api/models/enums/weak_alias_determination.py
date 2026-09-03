from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WeakAliasDetermination(str, Enum):
    """Names that are explicitly marked as low quality either by their ``source`` list, or by ``plaid`` by a series of
    additional checks done by Plaid. Plaid does not ever surface a hit as a result of a weak name alone. If a name has
    no quality issues, this value will be ``none``."""

    NONE = "none"
    SOURCE = "source"
    PLAID = "plaid"

    __str__ = str.__str__


WeakAliasDeterminationOrStr: TypeAlias = Annotated[
    WeakAliasDetermination | str, open_enum_validator(WeakAliasDetermination)
]
