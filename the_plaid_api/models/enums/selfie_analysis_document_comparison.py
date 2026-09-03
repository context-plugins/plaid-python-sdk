from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SelfieAnalysisDocumentComparison(str, Enum):
    """Information about the comparison between the selfie and the document (if documentary verification also ran)."""

    MATCH = "match"
    NO_MATCH = "no_match"
    NO_INPUT = "no_input"

    __str__ = str.__str__


SelfieAnalysisDocumentComparisonOrStr: TypeAlias = Annotated[
    SelfieAnalysisDocumentComparison | str, open_enum_validator(SelfieAnalysisDocumentComparison)
]
