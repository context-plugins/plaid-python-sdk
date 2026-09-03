from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxIncomeFireWebhookResponse(SdkBaseModel):
    """SandboxIncomeFireWebhookResponse defines the response schema for ``/sandbox/income/fire_webhook``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxIncomeFireWebhookResponseDict(TypedDict):
    request_id: str
