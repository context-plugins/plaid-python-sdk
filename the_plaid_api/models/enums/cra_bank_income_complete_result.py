from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CraBankIncomeCompleteResult(str, Enum):
    """The result of the bank income report generation

    ``SUCCESS``: The bank income report was successfully generated and can be retrieved via ``/credit/bank_income/get``.

    ``FAILURE``: The bank income report failed to be generated"""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    __str__ = str.__str__


CraBankIncomeCompleteResultOrStr: TypeAlias = Annotated[
    CraBankIncomeCompleteResult | str, open_enum_validator(CraBankIncomeCompleteResult)
]
