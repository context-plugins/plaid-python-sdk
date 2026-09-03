from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoanAccountSubtype(str, Enum):
    """Valid account subtypes for loan accounts. For a list containing descriptions of each subtype, see `Account
    schemas <https://plaid.com/docs/api/accounts/#StandaloneAccountType-loan>`__."""

    AUTO = "auto"
    BUSINESS = "business"
    COMMERCIAL = "commercial"
    CONSTRUCTION = "construction"
    CONSUMER = "consumer"
    HOME_EQUITY = "home equity"
    LOAN = "loan"
    MORTGAGE = "mortgage"
    OVERDRAFT = "overdraft"
    LINE_OF_CREDIT = "line of credit"
    STUDENT = "student"
    OTHER = "other"
    ALL = "all"

    __str__ = str.__str__


LoanAccountSubtypeOrStr: TypeAlias = Annotated[LoanAccountSubtype | str, open_enum_validator(LoanAccountSubtype)]
