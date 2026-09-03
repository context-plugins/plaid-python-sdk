from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LinkDeliveryWebhookCommunicationMethod(str, Enum):
    """The communication method used to deliver the Hosted Link session"""

    SMS = "SMS"
    EMAIL = "EMAIL"

    __str__ = str.__str__


LinkDeliveryWebhookCommunicationMethodOrStr: TypeAlias = Annotated[
    LinkDeliveryWebhookCommunicationMethod | str, open_enum_validator(LinkDeliveryWebhookCommunicationMethod)
]
