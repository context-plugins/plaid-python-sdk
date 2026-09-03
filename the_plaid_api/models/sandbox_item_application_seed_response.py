from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SandboxItemApplicationSeedResponse(SdkBaseModel):
    """SandboxItemApplicationSeedResponse defines the response schema for ``/sandbox/item/application/seed``"""

    item_id: str
    """The ``item_id`` of the newly seeded item representing the application connection."""

    request_id: str
    """A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid
    identifiers, is case sensitive."""


class SandboxItemApplicationSeedResponseDict(TypedDict):
    item_id: str
    request_id: str
