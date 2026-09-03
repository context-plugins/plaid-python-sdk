from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrismDetectVersion(str, Enum):
    """The version of Prism Detect"""

    _4_1 = "4.1"
    """The ``4.1`` Prism Detect version."""

    _4 = "4"
    """The ``4`` Prism Detect version."""

    __str__ = str.__str__


PrismDetectVersionOrStr: TypeAlias = Annotated[PrismDetectVersion | str, open_enum_validator(PrismDetectVersion)]
