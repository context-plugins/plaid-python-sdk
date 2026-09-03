from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.webhook_code import WebhookCodeOrStr
from .enums.webhook_type import WebhookTypeOrStr


class SandboxItemFireWebhookRequest(SdkBaseModel):
    """SandboxItemFireWebhookRequest defines the request schema for ``/sandbox/item/fire_webhook``"""

    client_id: Optional[str] = UNSET
    """Your Plaid API ``client_id``. The ``client_id`` is required and may be provided either in the ``PLAID-CLIENT-ID``
    header or as part of a request body."""

    secret: Optional[str] = UNSET
    """Your Plaid API ``secret``. The ``secret`` is required and may be provided either in the ``PLAID-SECRET`` header
    or as part of a request body."""

    access_token: str
    """The access token associated with the Item for which data is being requested."""

    webhook_type: Optional[WebhookTypeOrStr] = UNSET
    """The webhook types that can be fired by this test endpoint."""

    webhook_code: WebhookCodeOrStr
    """The webhook codes that can be fired by this test endpoint."""


class SandboxItemFireWebhookRequestDict(TypedDict):
    client_id: NotRequired[str]
    secret: NotRequired[str]
    access_token: str
    webhook_type: NotRequired[WebhookTypeOrStr]
    webhook_code: WebhookCodeOrStr
