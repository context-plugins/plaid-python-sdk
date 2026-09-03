from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkDeliveryDeliveryMethod(str, Enum):
    """The delivery method to be used to deliver the Hosted Link session URL.

    ``SMS``: The URL will be delivered through SMS

    ``EMAIL``: The URL will be delivered through email"""

    SMS = "SMS"
    EMAIL = "EMAIL"

    __str__ = str.__str__


LinkDeliveryDeliveryMethodOrStr: TypeAlias = Annotated[
    LinkDeliveryDeliveryMethod | str, open_enum_validator(LinkDeliveryDeliveryMethod)
]
