from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookEnvironmentValues(str, Enum):
    """The Plaid environment the webhook was sent from"""

    SANDBOX = "sandbox"
    PRODUCTION = "production"

    __str__ = str.__str__


WebhookEnvironmentValuesOrStr: TypeAlias = Annotated[
    WebhookEnvironmentValues | str, open_enum_validator(WebhookEnvironmentValues)
]
