from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrismFirstDetectVersion(str, Enum):
    """The version of Prism FirstDetect. If not specified, will default to v3."""

    _3 = "3"
    """The ``3`` Prism FirstDetect version."""

    __str__ = str.__str__


PrismFirstDetectVersionOrStr: TypeAlias = Annotated[
    PrismFirstDetectVersion | str, open_enum_validator(PrismFirstDetectVersion)
]
