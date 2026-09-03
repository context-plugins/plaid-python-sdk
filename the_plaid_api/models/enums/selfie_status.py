from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SelfieStatus(str, Enum):
    """An outcome status for this specific selfie. Distinct from the overall ``selfie_check.status`` that summarizes the
    verification outcome from one or more selfies."""

    SUCCESS = "success"
    FAILED = "failed"

    __str__ = str.__str__


SelfieStatusOrStr: TypeAlias = Annotated[SelfieStatus | str, open_enum_validator(SelfieStatus)]
