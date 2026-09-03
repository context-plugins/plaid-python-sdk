from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NotificationType(str, Enum):
    """Type of Notification"""

    ACCOUNT_TAKEOVER = "ACCOUNT_TAKEOVER"
    ADDRESS_CHANGED = "ADDRESS_CHANGED"
    BALANCE = "BALANCE"
    CONSENT_EXPIRED = "CONSENT_EXPIRED"
    CONSENT_GRANTED = "CONSENT_GRANTED"
    CONSENT_REVOKED = "CONSENT_REVOKED"
    CONSENT_UPDATED = "CONSENT_UPDATED"
    CUSTOM = "CUSTOM"
    MFA_TARGET_CHANGED = "MFA_TARGET_CHANGED"
    PHONE_CHANGED = "PHONE_CHANGED"
    PLANNED_OUTAGE = "PLANNED_OUTAGE"
    RISK = "RISK"
    SERVICE = "SERVICE"
    SUSPECTED_INCIDENT = "SUSPECTED_INCIDENT"
    TAN_ACTIVATED = "TAN_ACTIVATED"
    TAN_CREATED = "TAN_CREATED"
    TAN_REVOKED = "TAN_REVOKED"
    TAN_SUSPENDED = "TAN_SUSPENDED"

    __str__ = str.__str__


NotificationTypeOrStr: TypeAlias = Annotated[NotificationType | str, open_enum_validator(NotificationType)]
