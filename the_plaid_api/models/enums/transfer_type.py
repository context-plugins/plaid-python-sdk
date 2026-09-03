from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferType(str, Enum):
    """The type of transfer. This will be either ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account."""

    DEBIT = "debit"
    CREDIT = "credit"

    __str__ = str.__str__


TransferTypeOrStr: TypeAlias = Annotated[TransferType | str, open_enum_validator(TransferType)]
