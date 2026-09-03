from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.notification_category import NotificationCategoryOrStr
from .enums.notification_priority import NotificationPriorityOrStr
from .enums.notification_severity import NotificationSeverityOrStr
from .enums.notification_type import NotificationTypeOrStr
from .hateoas_link import HateoasLink, HateoasLinkDict
from .notification_payload_entity import NotificationPayloadEntity, NotificationPayloadEntityDict
from .party_entity import PartyEntity, PartyEntityDict


class FdxNotificationEntity(SdkBaseModel):
    """Provides the base fields of a notification. Clients will read the ``type`` property to determine the expected
    notification payload."""

    notification_id: str = Field(alias="notificationId")
    """Id of notification"""

    type_: NotificationTypeOrStr = Field(alias="type")
    """Type of Notification"""

    subtype: Optional[str] = UNSET
    """An optional initiator-defined event subtype code or description if the event type needs to be further categorized
    or described."""

    sent_on: RFC3339DateTime = Field(alias="sentOn")
    """ISO 8601 date-time in format 'YYYY-MM-DDThh:mm:ss.nnn[Z|[+|-]hh:mm]' according to `IETF RFC3339
    <https://datatracker.ietf.org/doc/html/rfc3339>`__"""

    category: NotificationCategoryOrStr
    """Category of Notification"""

    severity: Optional[NotificationSeverityOrStr] = UNSET
    """Severity level of notification"""

    priority: Optional[NotificationPriorityOrStr] = UNSET
    """Priority of notification"""

    publisher: Optional[PartyEntity] = UNSET
    """FDX Participant - an entity or person that is a part of a FDX API transaction"""

    subscriber: Optional[PartyEntity] = UNSET
    """FDX Participant - an entity or person that is a part of a FDX API transaction"""

    notification_payload: NotificationPayloadEntity = Field(alias="notificationPayload")
    """Custom key-value pairs payload for a notification"""

    url: Optional[HateoasLink] = UNSET
    """REST application constraint (Hypermedia As The Engine Of Application State)"""


class FdxNotificationEntityDict(TypedDict):
    notification_id: str
    type_: NotificationTypeOrStr
    subtype: NotRequired[str]
    sent_on: RFC3339DateTime
    category: NotificationCategoryOrStr
    severity: NotRequired[NotificationSeverityOrStr]
    priority: NotRequired[NotificationPriorityOrStr]
    publisher: NotRequired[PartyEntity | PartyEntityDict]
    subscriber: NotRequired[PartyEntity | PartyEntityDict]
    notification_payload: NotificationPayloadEntity | NotificationPayloadEntityDict
    url: NotRequired[HateoasLink | HateoasLinkDict]
