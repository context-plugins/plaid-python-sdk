from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookCode(str, Enum):
    """The webhook codes that can be fired by this test endpoint."""

    DEFAULT_UPDATE = "DEFAULT_UPDATE"
    NEW_ACCOUNTS_AVAILABLE = "NEW_ACCOUNTS_AVAILABLE"
    SMS_MICRODEPOSITS_VERIFICATION = "SMS_MICRODEPOSITS_VERIFICATION"
    AUTHORIZATION_GRANTED = "AUTHORIZATION_GRANTED"
    USER_PERMISSION_REVOKED = "USER_PERMISSION_REVOKED"
    USER_ACCOUNT_REVOKED = "USER_ACCOUNT_REVOKED"
    PENDING_DISCONNECT = "PENDING_DISCONNECT"
    RECURRING_TRANSACTIONS_UPDATE = "RECURRING_TRANSACTIONS_UPDATE"
    LOGIN_REPAIRED = "LOGIN_REPAIRED"
    SYNC_UPDATES_AVAILABLE = "SYNC_UPDATES_AVAILABLE"
    PRODUCT_READY = "PRODUCT_READY"
    ERROR = "ERROR"

    __str__ = str.__str__


WebhookCodeOrStr: TypeAlias = Annotated[WebhookCode | str, open_enum_validator(WebhookCode)]
