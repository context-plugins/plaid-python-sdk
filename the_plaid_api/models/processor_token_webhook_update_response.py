from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ProcessorTokenWebhookUpdateResponse(SdkBaseModel):
    """ProcessorTokenWebhookUpdateResponse defines the response schema for ``/processor/token/webhook/update``"""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class ProcessorTokenWebhookUpdateResponseDict(TypedDict):
    request_id: str
