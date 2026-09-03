from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferEventListTransferType(str, Enum):
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    your origination account; a ``credit`` indicates a transfer of money out of your origination account."""

    DEBIT = "debit"
    CREDIT = "credit"

    __str__ = str.__str__


TransferEventListTransferTypeOrStr: TypeAlias = Annotated[
    TransferEventListTransferType | str, open_enum_validator(TransferEventListTransferType)
]
