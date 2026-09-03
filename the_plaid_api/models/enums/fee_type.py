from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FeeType(str, Enum):
    """Fees on the account, e.g. commission, bookkeeping, options-related."""

    ACCOUNT_FEE = "account fee"
    ADJUSTMENT = "adjustment"
    DIVIDEND = "dividend"
    INTEREST = "interest"
    INTEREST_RECEIVABLE = "interest receivable"
    LONG_TERM_CAPITAL_GAIN = "long-term capital gain"
    LEGAL_FEE = "legal fee"
    MANAGEMENT_FEE = "management fee"
    MARGIN_EXPENSE = "margin expense"
    NON_QUALIFIED_DIVIDEND = "non-qualified dividend"
    NON_RESIDENT_TAX = "non-resident tax"
    QUALIFIED_DIVIDEND = "qualified dividend"
    RETURN_OF_PRINCIPAL = "return of principal"
    SHORT_TERM_CAPITAL_GAIN = "short-term capital gain"
    STOCK_DISTRIBUTION = "stock distribution"
    TAX = "tax"
    TAX_WITHHELD = "tax withheld"
    TRANSFER_FEE = "transfer fee"
    TRUST_FEE = "trust fee"
    UNQUALIFIED_GAIN = "unqualified gain"

    __str__ = str.__str__


FeeTypeOrStr: TypeAlias = Annotated[FeeType | str, open_enum_validator(FeeType)]
