from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ConsumerReportCategory(str, Enum):
    """Type of data being disputed by the consumer"""

    TRANSACTION = "TRANSACTION"
    BALANCE = "BALANCE"
    IDENTITY = "IDENTITY"
    OTHER = "OTHER"

    __str__ = str.__str__


ConsumerReportCategoryOrStr: TypeAlias = Annotated[
    ConsumerReportCategory | str, open_enum_validator(ConsumerReportCategory)
]
