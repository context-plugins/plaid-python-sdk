from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxItemFireWebhookResponse(SdkBaseModel):
    """SandboxItemFireWebhookResponse defines the response schema for ``/sandbox/item/fire_webhook``"""

    webhook_fired: bool
    """Value is ``true`` if the test ``webhook_code`` was successfully fired."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxItemFireWebhookResponseDict(TypedDict):
    webhook_fired: bool
    request_id: str
