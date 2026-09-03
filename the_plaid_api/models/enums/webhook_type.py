from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookType(str, Enum):
    """The webhook types that can be fired by this test endpoint."""

    AUTH = "AUTH"
    HOLDINGS = "HOLDINGS"
    INVESTMENTS_TRANSACTIONS = "INVESTMENTS_TRANSACTIONS"
    ITEM = "ITEM"
    LIABILITIES = "LIABILITIES"
    TRANSACTIONS = "TRANSACTIONS"
    ASSETS = "ASSETS"

    __str__ = str.__str__


WebhookTypeOrStr: TypeAlias = Annotated[WebhookType | str, open_enum_validator(WebhookType)]
