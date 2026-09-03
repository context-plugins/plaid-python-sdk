from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ImageQualityOutcome(str, Enum):
    """The outcome of the image quality check.


    ``success`` - The check passed.

    ``failed`` - The check did not pass."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


ImageQualityOutcomeOrStr: TypeAlias = Annotated[ImageQualityOutcome | str, open_enum_validator(ImageQualityOutcome)]
