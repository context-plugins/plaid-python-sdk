from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankIncomeRefreshCompleteResult(str, Enum):
    """The result of the bank income refresh report generation

    ``SUCCESS``: The refreshed report was successfully generated and can be retrieved via ``/credit/bank_income/get``.

    ``FAILURE``: The refreshed report failed to be generated"""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    __str__ = str.__str__


BankIncomeRefreshCompleteResultOrStr: TypeAlias = Annotated[
    BankIncomeRefreshCompleteResult | str, open_enum_validator(BankIncomeRefreshCompleteResult)
]
