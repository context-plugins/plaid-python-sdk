from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status4(str, Enum):
    """This field is deprecated in favor of the ``breakdown`` object, which provides more granular institution health
    data.

    ``HEALTHY``: the majority of requests are successful ``DEGRADED``: only some requests are successful ``DOWN``: all
    requests are failing"""

    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    DOWN = "DOWN"

    __str__ = str.__str__


Status4OrStr: TypeAlias = Annotated[Status4 | str, open_enum_validator(Status4)]
