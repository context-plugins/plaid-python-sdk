from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankTransferEventListBankTransferType(str, Enum):
    """The type of bank transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money
    into your origination account; a ``credit`` indicates a transfer of money out of your origination account."""

    DEBIT = "debit"
    CREDIT = "credit"

    __str__ = str.__str__


BankTransferEventListBankTransferTypeOrStr: TypeAlias = Annotated[
    BankTransferEventListBankTransferType | str, open_enum_validator(BankTransferEventListBankTransferType)
]
