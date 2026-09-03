from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentChannel(str, Enum):
    """The channel used to make a payment. ``online:`` transactions that took place online.

    ``in store:`` transactions that were made at a physical location.

    ``other:`` transactions that relate to banks, e.g. fees or deposits.

    This field replaces the ``transaction_type`` field."""

    ONLINE = "online"
    IN_STORE = "in store"
    OTHER = "other"

    __str__ = str.__str__


PaymentChannelOrStr: TypeAlias = Annotated[PaymentChannel | str, open_enum_validator(PaymentChannel)]
