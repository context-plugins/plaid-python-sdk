from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraPartnerInsightsUltraFicoScoreVersion(str, Enum):
    """The version of the UltraFICO® score."""

    _1_0 = "1.0"
    """The ``1.0`` UltraFICO score version."""

    __str__ = str.__str__


CraPartnerInsightsUltraFicoScoreVersionOrStr: TypeAlias = Annotated[
    CraPartnerInsightsUltraFicoScoreVersion | str, open_enum_validator(CraPartnerInsightsUltraFicoScoreVersion)
]
