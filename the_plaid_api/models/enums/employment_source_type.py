from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EmploymentSourceType(str, Enum):
    """The types of source employment data that users should be able to share"""

    BANK = "bank"
    PAYROLL = "payroll"

    __str__ = str.__str__


EmploymentSourceTypeOrStr: TypeAlias = Annotated[EmploymentSourceType | str, open_enum_validator(EmploymentSourceType)]
