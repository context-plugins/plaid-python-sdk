from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraPartnerInsightsBaseFicoScoreVersion(str, Enum):
    """The version of the base FICO score model."""

    _8 = "8"
    """The ``8`` base FICO score version."""

    _9 = "9"
    """The ``9`` base FICO score version."""

    _10 = "10"
    """The ``10`` base FICO score version."""

    _10_T = "10T"
    """The ``10T`` base FICO score version."""

    __str__ = str.__str__


CraPartnerInsightsBaseFicoScoreVersionOrStr: TypeAlias = Annotated[
    CraPartnerInsightsBaseFicoScoreVersion | str, open_enum_validator(CraPartnerInsightsBaseFicoScoreVersion)
]
