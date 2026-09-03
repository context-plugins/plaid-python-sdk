from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrismInsightsVersion(str, Enum):
    """The version of Prism Insights. If not specified, will default to v3."""

    _4_1 = "4.1"
    """The ``4.1`` Prism Insights version."""

    _4 = "4"
    """The ``4`` Prism Insights version."""

    _3 = "3"
    """The ``3`` Prism Insights version."""

    __str__ = str.__str__


PrismInsightsVersionOrStr: TypeAlias = Annotated[PrismInsightsVersion | str, open_enum_validator(PrismInsightsVersion)]
