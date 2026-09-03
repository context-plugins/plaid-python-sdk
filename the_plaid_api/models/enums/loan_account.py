from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoanAccount(str, Enum):
    """A loan type account."""

    AUTO = "auto"
    BUSINESS = "business"
    COMMERCIAL = "commercial"
    CONSTRUCTION = "construction"
    CONSUMER = "consumer"
    HOME_EQUITY = "home equity"
    LINE_OF_CREDIT = "line of credit"
    LOAN = "loan"
    MORTGAGE = "mortgage"
    OTHER = "other"
    OVERDRAFT = "overdraft"
    STUDENT = "student"

    __str__ = str.__str__


LoanAccountOrStr: TypeAlias = Annotated[LoanAccount | str, open_enum_validator(LoanAccount)]
