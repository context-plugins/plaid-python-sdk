from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankIncomeCompleteResult(str, Enum):
    """The result of the bank income report generation

    ``SUCCESS``: The bank income report was successfully generated and can be retrieved via ``/credit/bank_income/get``.

    ``FAILURE``: The bank income report failed to be generated"""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    __str__ = str.__str__


BankIncomeCompleteResultOrStr: TypeAlias = Annotated[
    BankIncomeCompleteResult | str, open_enum_validator(BankIncomeCompleteResult)
]
