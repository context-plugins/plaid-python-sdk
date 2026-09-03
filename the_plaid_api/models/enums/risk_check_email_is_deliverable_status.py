from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskCheckEmailIsDeliverableStatus(str, Enum):
    """SMTP-MX check to confirm the email address exists if known."""

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    __str__ = str.__str__


RiskCheckEmailIsDeliverableStatusOrStr: TypeAlias = Annotated[
    RiskCheckEmailIsDeliverableStatus | str, open_enum_validator(RiskCheckEmailIsDeliverableStatus)
]
