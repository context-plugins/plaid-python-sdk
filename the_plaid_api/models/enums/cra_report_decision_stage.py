from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraReportDecisionStage(str, Enum):
    """The stage in the lending lifecycle for which the report is being retrieved."""

    PREQUALIFICATION = "PREQUALIFICATION"
    DECISIONING = "DECISIONING"
    SERVICING = "SERVICING"

    __str__ = str.__str__


CraReportDecisionStageOrStr: TypeAlias = Annotated[
    CraReportDecisionStage | str, open_enum_validator(CraReportDecisionStage)
]
