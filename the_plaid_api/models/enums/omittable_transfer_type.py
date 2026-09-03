from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OmittableTransferType(str, Enum):
    """The type of transfer. Valid values are ``debit`` or ``credit``. A ``debit`` indicates a transfer of money into
    the origination account; a ``credit`` indicates a transfer of money out of the origination account. This field is
    omitted for Plaid Ledger Sweep events."""

    DEBIT = "debit"
    CREDIT = "credit"

    __str__ = str.__str__


OmittableTransferTypeOrStr: TypeAlias = Annotated[
    OmittableTransferType | str, open_enum_validator(OmittableTransferType)
]
