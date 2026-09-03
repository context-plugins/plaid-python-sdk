from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SelfieAnalysisFacialAnalysisOutcome(str, Enum):
    """Outcome of the facial analysis for a specific facial feature."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


SelfieAnalysisFacialAnalysisOutcomeOrStr: TypeAlias = Annotated[
    SelfieAnalysisFacialAnalysisOutcome | str, open_enum_validator(SelfieAnalysisFacialAnalysisOutcome)
]
