from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NetworkInsightsVersion(str, Enum):
    """The version of Network Insights. Required if using Network Insights."""

    NI1 = "NI1"

    __str__ = str.__str__


NetworkInsightsVersionOrStr: TypeAlias = Annotated[
    NetworkInsightsVersion | str, open_enum_validator(NetworkInsightsVersion)
]
