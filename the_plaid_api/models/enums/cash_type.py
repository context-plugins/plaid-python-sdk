from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CashType(str, Enum):
    """Activity that modifies a cash position"""

    ACCOUNT_FEE = "account fee"
    CONTRIBUTION = "contribution"
    DEPOSIT = "deposit"
    DIVIDEND = "dividend"
    STOCK_DISTRIBUTION = "stock distribution"
    INTEREST = "interest"
    LEGAL_FEE = "legal fee"
    LONG_TERM_CAPITAL_GAIN = "long-term capital gain"
    MANAGEMENT_FEE = "management fee"
    MARGIN_EXPENSE = "margin expense"
    NON_QUALIFIED_DIVIDEND = "non-qualified dividend"
    NON_RESIDENT_TAX = "non-resident tax"
    PENDING_CREDIT = "pending credit"
    PENDING_DEBIT = "pending debit"
    QUALIFIED_DIVIDEND = "qualified dividend"
    SHORT_TERM_CAPITAL_GAIN = "short-term capital gain"
    TAX = "tax"
    TAX_WITHHELD = "tax withheld"
    TRANSFER_FEE = "transfer fee"
    TRUST_FEE = "trust fee"
    UNQUALIFIED_GAIN = "unqualified gain"
    WITHDRAWAL = "withdrawal"

    __str__ = str.__str__


CashTypeOrStr: TypeAlias = Annotated[CashType | str, open_enum_validator(CashType)]
