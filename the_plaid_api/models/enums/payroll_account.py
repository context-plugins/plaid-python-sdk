from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayrollAccount(str, Enum):
    """A payroll account."""

    PAYROLL = "payroll"

    __str__ = str.__str__


PayrollAccountOrStr: TypeAlias = Annotated[PayrollAccount | str, open_enum_validator(PayrollAccount)]
