from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxProcessorTokenCreateResponse(SdkBaseModel):
    """SandboxProcessorTokenCreateResponse defines the response schema for ``/sandbox/processor_token/create``"""

    processor_token: str
    """A processor token that can be used to call the ``/processor/`` endpoints."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxProcessorTokenCreateResponseDict(TypedDict):
    processor_token: str
    request_id: str
