from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SelfieAnalysisLivenessCheck(str, Enum):
    """Assessment of whether the selfie capture is of a real human being, as opposed to a picture of a human on a
    screen, a picture of a paper cut out, someone wearing a mask, or a deepfake."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


SelfieAnalysisLivenessCheckOrStr: TypeAlias = Annotated[
    SelfieAnalysisLivenessCheck | str, open_enum_validator(SelfieAnalysisLivenessCheck)
]
