from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .error import Error, ErrorDict
from .link_callback_metadata import LinkCallbackMetadata, LinkCallbackMetadataDict


class LinkDeliveryCallbackWebhook(SdkBaseModel):
    """Webhook containing metadata proxied over from Link callback e.g. ``onEvent``, ``onExit``, ``onSuccess``."""

    webhook_type: str
    """``LINK_DELIVERY``"""

    webhook_code: str
    """``LINK_CALLBACK``"""

    link_delivery_session_id: str
    """The ID of the Hosted Link session."""

    timestamp: str
    """Timestamp in `ISO 8601 <https://wikipedia.org/wiki/ISO_8601>`__ format."""

    error: OptionalNullable[Error] = UNSET
    """Errors are identified by ``error_code`` and categorized by ``error_type``. Use these in preference to HTTP status
    codes to identify and handle specific errors. HTTP status codes are set and provide the broadest categorization of
    errors: 4xx codes are for developer- or user-related errors, and 5xx codes are for Plaid-related errors, and the
    status will be 2xx in non-error cases. An Item with a non-``null`` error object will only be part of an API response
    when calling ``/item/get`` to view Item status. Otherwise, error fields will be ``null`` if no error has occurred;
    if an error has occurred, an error code will be returned instead."""

    link_callback_metadata: LinkCallbackMetadata
    """Information related to the callback from the Hosted Link session."""


class LinkDeliveryCallbackWebhookDict(TypedDict):
    webhook_type: str
    webhook_code: str
    link_delivery_session_id: str
    timestamp: str
    error: NotRequired[Error | ErrorDict | None]
    link_callback_metadata: LinkCallbackMetadata | LinkCallbackMetadataDict
