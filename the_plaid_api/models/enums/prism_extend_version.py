from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrismExtendVersion(str, Enum):
    """The version of Prism Extend"""

    _4_1 = "4.1"
    """The ``4.1`` Prism Extend version."""

    _4 = "4"
    """The ``4`` Prism Extend version."""

    __str__ = str.__str__


PrismExtendVersionOrStr: TypeAlias = Annotated[PrismExtendVersion | str, open_enum_validator(PrismExtendVersion)]
