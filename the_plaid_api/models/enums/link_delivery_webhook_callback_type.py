from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkDeliveryWebhookCallbackType(str, Enum):
    """The type of Link callback event"""

    ON_SUCCESS = "ON_SUCCESS"
    ON_EVENT = "ON_EVENT"
    ON_EXIT = "ON_EXIT"

    __str__ = str.__str__


LinkDeliveryWebhookCallbackTypeOrStr: TypeAlias = Annotated[
    LinkDeliveryWebhookCallbackType | str, open_enum_validator(LinkDeliveryWebhookCallbackType)
]
