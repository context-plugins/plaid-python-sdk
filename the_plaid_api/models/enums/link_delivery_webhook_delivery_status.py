from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkDeliveryWebhookDeliveryStatus(str, Enum):
    """The status of the delivery of the Hosted Link to the user"""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    __str__ = str.__str__


LinkDeliveryWebhookDeliveryStatusOrStr: TypeAlias = Annotated[
    LinkDeliveryWebhookDeliveryStatus | str, open_enum_validator(LinkDeliveryWebhookDeliveryStatus)
]
