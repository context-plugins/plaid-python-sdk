from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel


class ItemStatusLastWebhook(SdkBaseModel):
    """Information about the last webhook fired for the Item."""

    sent_at: OptionalNullable[RFC3339DateTime] = UNSET
    """`ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ timestamp of when the webhook was fired."""

    code_sent: Optional[str] = UNSET
    """The last webhook code sent."""


class ItemStatusLastWebhookDict(TypedDict):
    sent_at: NotRequired[RFC3339DateTime | None]
    code_sent: NotRequired[str]
