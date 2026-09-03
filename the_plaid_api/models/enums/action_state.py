from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ActionState(str, Enum):
    """Enum representing the state of the action/activity."""

    UNKNOWN = "UNKNOWN"
    ATTEMPT = "ATTEMPT"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    SKIPPED = "SKIPPED"

    __str__ = str.__str__


ActionStateOrStr: TypeAlias = Annotated[ActionState | str, open_enum_validator(ActionState)]
