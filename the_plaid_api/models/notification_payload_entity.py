from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.notification_payload_id_type import NotificationPayloadIdTypeOrStr
from .fdx_lifecycle_event_entity import FdxLifecycleEventEntity, FdxLifecycleEventEntityDict


class NotificationPayloadEntity(SdkBaseModel):
    """Custom key-value pairs payload for a notification"""

    id: Optional[str] = UNSET
    """ID for the origination entity related to the notification"""

    id_type: Optional[NotificationPayloadIdTypeOrStr] = Field(default=UNSET, alias="idType")
    """Type of entity causing origination of a notification"""

    event: Optional[FdxLifecycleEventEntity] = UNSET
    """Details of consent or payment network identifier or other entity's revocation request or other lifecycle status
    change event"""


class NotificationPayloadEntityDict(TypedDict):
    id: NotRequired[str]
    id_type: NotRequired[NotificationPayloadIdTypeOrStr]
    event: NotRequired[FdxLifecycleEventEntityDict]
