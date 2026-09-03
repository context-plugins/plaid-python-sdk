from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FlowType(str, Enum):
    """This field has been deprecated in favor of ``auth_type_select_enabled``."""

    FLEXIBLE_AUTH = "FLEXIBLE_AUTH"

    __str__ = str.__str__


FlowTypeOrStr: TypeAlias = Annotated[FlowType | str, open_enum_validator(FlowType)]
